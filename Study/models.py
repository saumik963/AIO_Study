from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
