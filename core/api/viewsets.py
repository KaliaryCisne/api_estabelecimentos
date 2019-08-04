from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Estabelecimento
from .serializers import EstabelecimentoSerializer

class EstabelecimentoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = EstabelecimentoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', '^produtos__nome']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Estabelecimento.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    # Retorna uma lista de recursos
    def list(self, request, *args, **kwargs):
        return super(EstabelecimentoViewSet, self).list(request, *args, **kwargs)

    # Chamado no Post
    def create(self, request, *args, **kwargs):
        super(EstabelecimentoViewSet, self).create(request, *args, **kwargs)
        return Response({'Result': 'Estabelecimento adcionado com sucesso!'})

    # Chamado no delete
    def destroy(self, request, *args, **kwargs):
        try:
            super(EstabelecimentoViewSet, self).destroy(request, *args, **kwargs)
            return Response({'Result': 'Estabelecimento deletado com sucesso!'})
        except Http404:
            return Response('Objeto nao deletado!')
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Validação sobre o get, salvar logs
    def retrieve(self, request,  *args, **kwargs):
        return super(EstabelecimentoViewSet, self).retrieve(request, *args, **kwargs)

    # chamado no put
    def update(self, request, *args, **kwargs):
        return super(EstabelecimentoViewSet, self).update(request, *args, **kwargs)

    # chamado no patch
    def partial_update(self, request, *args, **kwargs):
        return super(EstabelecimentoViewSet, self).partial_update(request, *args, **kwargs)

    # Detail igual a False quer dizer que essa funcao é relacionado ao endpoint
    # e não a um recurso do endpoint
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass