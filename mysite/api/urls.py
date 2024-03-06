from django.urls import path
from .views import ArticlesList, AirportViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('articles/', ArticlesList.as_view()),
]

router = DefaultRouter()
router.register('articles2', AirportViewSet, basename='articles')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns += router.urls