from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Estabelecimento
from .serializers import EstabelecimentoSerializer

class EstabelecimentoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = EstabelecimentoSerializer

    def get_queryset(self):
        return Estabelecimento.objects.filter(aprovado=True)

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