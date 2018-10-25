from django.shortcuts import render


from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Article, Entry
from. serializers import ArticleSerializer, EntrySerializer


def home(request):
    return render(request, 'home.html')


class ArticleViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(detail=True, methods=['get'])
    def entries(self, request, pk=None):
        article = self.get_object()
        serializer = EntrySerializer(article.entry_set.all(), many=True)
        return Response(serializer.data)


class EntryViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
