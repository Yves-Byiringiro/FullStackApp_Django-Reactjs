# from rest_framework import generics
from .serializers import ArticleSerializer
from articles.models import Article
from rest_framework import viewsets



class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()





# class ArticleListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleCreateView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateView(generics.UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleDeleteView(generics.DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
