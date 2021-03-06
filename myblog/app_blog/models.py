from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    # If a user is deleted, delete all posts - Not Vice Versa
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
