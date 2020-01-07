from django.urls import path, include
from rest_framework import routers
from tracker.views import MoodRecordViewSet, receive_record_sms

router = routers.SimpleRouter()
router.register(r"records", MoodRecordViewSet, basename="record")

urlpatterns = [
    path("sms", receive_record_sms)
]

urlpatterns += router.urls
