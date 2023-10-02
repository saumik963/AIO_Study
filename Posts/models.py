from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PostTitle = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000)

    image = models.ImageField(blank=True, upload_to='media/photos')

    is_post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.PostTitle} - {self.user}"
