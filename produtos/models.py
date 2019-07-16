from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.nome