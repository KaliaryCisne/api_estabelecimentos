from rest_framework.viewsets import ModelViewSet
from core.models import Estabelecimento
from .serializers import EstabelecimentoSerializer

class EstabelecimentoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
