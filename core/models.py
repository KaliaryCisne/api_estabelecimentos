from django.db import models
from produtos.models import Produto
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco



class Estabelecimento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    produtos = models.ManyToManyField(Produto)
    aprovado = models.BooleanField(default=False)
    comentarios = models.ManyToManyField(Comentario)
    avaliacaoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='estabelecimentos', null=True, blank=True)


    def __str__(self):
        return self.nome