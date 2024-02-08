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
<<<<<<< HEAD
        fields = ['images']
=======
        fields = ['images']
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
