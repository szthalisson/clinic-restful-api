from django.db import models


class Doctor(models.Model):
  cpf = models.CharField(max_length=15, verbose_name='CPF', unique=True)
  name = models.CharField(max_length=100, verbose_name='Nome')
  admission = models.DateTimeField(verbose_name='Data de admissão')
  wage = models.FloatField(verbose_name='Salário', default=4000)

  class Meta:
    verbose_name = 'Doutor'
    verbose_name_plural = 'Doutores'
    ordering = ['name']

  def __str__(self):
    return self.name
  

class Patient(models.Model):
  code = models.IntegerField(null=True, blank=True, unique=True, verbose_name='Código')
  name = models.CharField(max_length=100, verbose_name='Nome')
  cpf = models.CharField(max_length=15, verbose_name='CPF')
  address = models.TextField(verbose_name='Endereço')
  phone = models.CharField(max_length=15, verbose_name='Telefone')
  date_birth = models.DateField(verbose_name='Data de nascimento')

  class Meta:
    verbose_name = 'Paciente'
    ordering = ['code']

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    if not self.code:
      last_code = Patient.objects.order_by('-code').values_list('code', flat=True).first()
      self.code = (last_code + 1) if last_code else 100
    super().save(*args, **kwargs)