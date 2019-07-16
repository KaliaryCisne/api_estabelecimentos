from django.db import models

class Endereco(models.Model):
    rua_numero = models.CharField(max_length=150, null=True, blank=True)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s, %s'%(self.rua_numero, self.bairro)
