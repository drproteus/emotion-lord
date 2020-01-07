import json
from django.http import HttpResponse
from tracker.models import MoodRecord, UserProfile
from django.views.generic import View
from django.urls.exceptions import Http404
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


class MoodRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodRecord
        fields = ["id", "user", "score", "description", "created_at", "updated_at"]
        read_only_fields = (
            "id",
            "user",
            "created_at",
        )


class MoodRecordViewSet(viewsets.ModelViewSet):
    serializer_class = MoodRecordSerializer

    def get_queryset(self):
        user = self.request.user
        return user.moodrecord_set.all()


class ProfileView(View):
    def get(self, request):
        if not request.user:
            raise Http404
        records = request.user.moodrecord_set.all()
        return render(
            request, "profile.html", context={"records": records, "user": request.user}
        )

@csrf_exempt
def receive_record_sms(request):
    resp = MessagingResponse()

    try:
        profile = UserProfile.objects.get(number=request.POST.get("From", None))    
    except UserProfile.DoesNotExist:
        resp.message("No account exists for this phone number.")
        return resp
    
    score = request.POST.get("Body", "").strip()
    try:
        score = int(score)
    except ValueError:
        resp.message("Please submit a single number between 0 and 10")
        return resp

    try:
        record = MoodRecord(score=score, user=profile.user)
        record.save()
    except Exception as e:
        resp.message("Sorry... Something went wrong making the record. Please try again in a few minutes or contact support. Thanks for your patience.")
    else:
        resp.message("Recorded {timestamp}".format(timestamp=record.created_at.strftime("%c")))

    return HttpResponse(resp)
    