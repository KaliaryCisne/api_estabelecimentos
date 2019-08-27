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


    # Esse método é colocado nos fields do serializer para ser visto
    @property
    def descricao_completa2(self):
        return '%s - %s' %(self.nome, self.descricao)



    def __str__(self):
        return self.nome