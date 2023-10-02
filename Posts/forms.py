from django import forms
from django.forms import widgets
from .models import Post


class PostForm(forms.ModelForm):
    image = forms.FileInput()

    class Meta:
        model = Post
        fields = ['PostTitle', 'Description', 'image', 'is_post']
