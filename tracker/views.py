from tracker.models import MoodRecord
from rest_framework import serializers, viewsets
from rest_framework.response import Response


class MoodRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodRecord
        fields = ["user", "score", "description", "created_at", "updated_at"]


class MoodRecordViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = request.current_user.moodrecord_set.all()
        serializer = MoodRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = request.current_user.moodrecord_set.all()
        try:
            record = queryset.get()
        except MoodRecord.DoesNotExist:
            return Response({"message": "Not found."}, status=404)
        serializer = MoodRecordSerializer(record)
        return Response(serializer.data)
