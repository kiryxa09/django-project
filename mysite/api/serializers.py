from rest_framework import serializers
from articles.models import Articles, Comment

class ArticlesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Articles
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  origin = ArticlesSerializer()
  class Meta:
    model = Comment
    exclude = ['created_at']