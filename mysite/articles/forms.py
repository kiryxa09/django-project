from django import forms
from .models import Articles

app_name = 'articles'

class ArticlesForm(forms.ModelForm):
  class Meta:
    model = Articles
    fields = '__all__'