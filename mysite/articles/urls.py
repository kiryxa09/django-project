from django.urls import path
from .views import index, articles, article, articles_filter


urlpatterns = [
  path('index/', index),
  path('', articles),
  path('articles_filter/', articles_filter, name='articles_filter'),
  path('<slug:slug>/', article, name='article'),
]