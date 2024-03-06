from articles.models import Articles, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ArticlesSerializer, CommentSerializer

from rest_framework import viewsets
# Create your views here.

class ArticlesList(APIView):
  def get(self, request):
    articles = Articles.objects.all()
    serializer = ArticlesSerializer(articles, many=True)
    return Response({'articles': serializer.data})
  
  def post(self, request):
      article = request.data.get('article')

      serializer = ArticlesSerializer(data=article)
      if serializer.is_valid(raise_exception=True):
          saved_data = serializer.save()
          return Response({"success": "Article {} created successfully".format(saved_data)}, status=201)
      else:
          return Response(serializer.errors)
  
  def delete(self, request, id):
      article = Articles.objects.get(id=id)
      article.delete()
      return Response({"message": "Article {} deleted successfully".format(article.title)})
      
      
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

