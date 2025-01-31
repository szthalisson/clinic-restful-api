from rest_framework import viewsets
from api.models import Doctor, Patient
from api.serializers import DoctorSerializer, PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
  queryset = Doctor.objects.all()
  serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
  queryset = Patient.objects.all()
  serializer_class = PatientSerializer