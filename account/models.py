from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('User must have a email')

        # Get 'email' from extra_fields or set it to an empty string

        user = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=500)
    dp = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
