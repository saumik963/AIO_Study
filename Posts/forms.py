from django import forms
from .models import Post,PostImages


class PostForm(forms.ModelForm):
    image = forms.FileInput()

    class Meta:
        model = Post
        fields = ['PostTitle', 'Description', 'Coverimage', 'is_post']

class PostImagesForm(forms.ModelForm):
    class Meta:
        model = PostImages
        fields = ['images']