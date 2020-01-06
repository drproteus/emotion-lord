from rest_framework import routers
from tracker.views import MoodRecordViewSet

router = routers.SimpleRouter()
router.register(r'records', MoodRecordViewSet, basename="record")

urlpatterns = router.urls