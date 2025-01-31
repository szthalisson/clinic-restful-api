from django.contrib import admin
from api.models import Doctor, Patient


class DoctorAdmin(admin.ModelAdmin):
  list_display = ['cpf', 'name', 'admission', 'wage']
  search_fields = ('name','cpf',)


class PatientAdmin(admin.ModelAdmin):
  list_display = ['code', 'name', 'phone']
  search_fields = ('code','name','cpf',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)