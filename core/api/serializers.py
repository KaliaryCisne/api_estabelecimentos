from rest_framework.serializers import ModelSerializer
from core.models import Estabelecimento
from produtos.api.serializers import ProdutoSerializer

#todo estudar SlugRelatedField para retornar o o nome dos produtos
class EstabelecimentoSerializer(ModelSerializer):

    # produtos = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='nome'
    # )

    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome', 'descricao', 'produtos', 'aprovado', 'foto')