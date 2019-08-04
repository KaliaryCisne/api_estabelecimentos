from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecosSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
    filterset_fields = ['rua_numero', 'cidade', 'bairro']