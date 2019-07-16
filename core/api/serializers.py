from rest_framework.serializers import ModelSerializer
from core.models import Estabelecimento

class EstabelecimentoSerializer(ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('nome', 'descricao', 'produto')