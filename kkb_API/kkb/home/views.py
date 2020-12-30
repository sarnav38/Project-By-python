from .models import Article
from .serializers import ArticleSerializers
from rest_framework import viewsets


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
