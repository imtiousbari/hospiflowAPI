from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WardViewSet, TeamViewSet, DoctorViewSet, PatientViewSet, TreatmentViewSet

router = DefaultRouter()
router.register(r'wards', WardViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'treatments', TreatmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
