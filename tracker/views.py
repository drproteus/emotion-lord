from tracker.models import MoodRecord
from django.views.generic import View
from django.urls.exceptions import Http404
from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.response import Response


class MoodRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodRecord
        fields = ["user", "score", "description", "created_at", "updated_at"]


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
        return render(request, "profile.html", context={
            "records": records, "user": request.user
        })
