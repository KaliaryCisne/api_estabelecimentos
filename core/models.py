from django.db import models
from produtos.models import Produto
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco



class Estabelecimento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    produto = models.ManyToManyField(Produto)
    aprovado = models.BooleanField(default=False)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome