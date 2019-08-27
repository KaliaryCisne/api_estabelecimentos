from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import Estabelecimento
from produtos.api.serializers import ProdutoSerializer
from enderecos.api.serializers import EnderecosSerializer

#todo estudar SlugRelatedField para retornar o o nome dos produtos
class EstabelecimentoSerializer(ModelSerializer):

    # NestedRelationsShips
    produtos = ProdutoSerializer(many=True)
    endereco = EnderecosSerializer(read_only=True)
    descricao_completa = SerializerMethodField()
  

    # É possível acessar um método do model e colocalo no field   

    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome', 'descricao', 'produtos',
         'aprovado', 'foto', 'endereco', 'descricao_completa', 'descricao_completa2'
         )
        read_only_fields = ('descricao', )
        

    def cria_produtos(self, produtos, estabelecimento):
        for produto in produtos:
            prod =  Produto.objects.create(**produto)
            estabelecimento.produtos.add(prod)

    def create(self, validated_data):
        produtos = validated_data['produtos']
        del validated_data['produtos']
        estabelecimento = Estabelecimento.objects.create(**validated_data)
        self.cria_produtos(produtos, estabelecimento)

        return estabelecimento

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)