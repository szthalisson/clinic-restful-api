from rest_framework.routers import DefaultRouter
from api.views import DoctorViewSet, PatientViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')
router.register(r'patients', PatientViewSet, basename='patients')

urlpatterns = [
  path('', include(router.urls))
]