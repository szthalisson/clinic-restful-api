from rest_framework.routers import DefaultRouter
from api.views import DoctorViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
  path('', include(router.urls))
]