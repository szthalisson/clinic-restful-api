from rest_framework import viewsets
from api.models import Doctor
from api.serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
  queryset = Doctor.objects.all()
  serializer_class = DoctorSerializer