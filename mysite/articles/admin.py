from django.contrib import admin
from .models import Articles, Comment



# Register your models here.
admin.site.register(Comment)

class CommentInline(admin.TabularInline):
  model = Comment
  fk_name = 'origin'
  extra = 1

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
  inlines = [
    CommentInline
  ]
  prepopulated_fields = {'slug': ('title',)}