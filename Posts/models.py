from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< HEAD
from ckeditor.fields import RichTextField
=======
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47

User = get_user_model()
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PostTitle = models.CharField(max_length=100)
<<<<<<< HEAD
    Description = RichTextField(null=True, blank=True)
=======
    Description = models.CharField(max_length=10000)
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47

    Coverimage = models.ImageField(blank=True, upload_to='CoverPhotos')

    is_post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.PostTitle} - {self.user}"

class PostImages(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='PostImages')

    def __str__(self) :
<<<<<<< HEAD
        return self.post.PostTitle
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
=======
        return self.post.PostTitle
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47
