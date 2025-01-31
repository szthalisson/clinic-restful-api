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