from django_filters import filters
from rest_framework.viewsets import ModelViewSet
from produtos.models import Produto
from .serializers import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filterset_fields = ['nome', 'descricao']
