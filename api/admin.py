from django.contrib import admin
from api.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
  list_display = ['cpf', 'name', 'admission', 'wage']
  search_fields = ('name','cpf',)

admin.site.register(Doctor, DoctorAdmin)