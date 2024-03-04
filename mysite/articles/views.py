from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articles, Comment
from django.contrib.auth.decorators import permission_required, login_required

# Create your views here.
def index(request):
  return HttpResponse('firstPage')

def articles(request):
  a = Articles.objects.all()
  context = {
    'articles': a
  }

  return render(request, 'articles.html', context)

def article(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    comments = Comment.objects.filter(origin=article.id).all()
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'article.html', context)
  
@login_required
def articles_filter(request):
    if request.method == "GET":
        name = request.GET.get('name')
        f = None
        if name:
            f = Articles.objects.filter(title__icontains=name).all()
        context = {
            'articles': f,
            'name': name
        }
    return render(request, 'articles_filter.html', context)