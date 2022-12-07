from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
   text = forms.CharField(min_length=20)
   class Meta:
       model = Post
       fields = [
           'authors',
           'title',
           'content_choice',
           'category',
           'text',
       ]

   def clean(self):
       cleaned_data = super().clean()
       name = cleaned_data.get('title')
       text = cleaned_data.get("text")
       if name == text:
           raise ValidationError(
               "Описание не должно быть идентично названию."
           )

       return cleaned_data