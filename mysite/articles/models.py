from django.db import models
from django.utils.timezone import now

# Create your models here.
class Articles(models.Model):
  title = models.CharField(max_length=100, verbose_name='Название статьи')
  author = models.CharField(max_length=250, verbose_name='Автор статьи')
  content = models.TextField(verbose_name='Текст статьи')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  slug = models.SlugField(verbose_name='URL', blank=True, null=True, unique=True)

  def __str__(self):
    return f'{self.title} {self.content}'
  
  def get_comments(self):
    return f'{self.comments_autor} {self.comments_text}'

class Comment(models.Model):
  origin = models.ForeignKey(Articles, default=1, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментируемая статья')
  author = models.CharField(max_length=250, verbose_name='Автор комментария')
  content = models.TextField(verbose_name='Текст комментария')
  created_at = models.DateTimeField(verbose_name='Дата создания', default=now)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'{self.author} {self.content}'