from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles, Comment

# Create your views here.
def index(request):
  return HttpResponse('firstPage')

def articles(request):
  a = Articles.objects.all()
  context = {
    'articles': a
  }

  return render(request, 'articles.html', context)

def article(request, article_id):
    article = Articles.objects.get(id=article_id)
    comments = Comment.objects.filter(origin=article_id).all()
    context = {
    'article': article,
    'comments': comments
    }
    return render(request,  'article.html', context)
  