
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    ACCESS_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')
    access = models.CharField(max_length=10, choices=ACCESS_CHOICES, default=PUBLIC)
    allowed_emails = models.TextField(blank=True, null=True)
