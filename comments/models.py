"""Comments"""

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Models

# Create your models here.
class Comment(models.Model):
    """Comment model."""
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return self.comment