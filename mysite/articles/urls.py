from django.urls import path
from .views import index, articles, article

urlpatterns = [
  path('index/', index),
  path('', articles),
  path('<int:article_id>/', article, name='article')
]