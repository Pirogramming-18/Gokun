from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()

class Comment(models.Model):
      comment = models.CharField(max_length=100)
  
class Like(models.Model):
  like = models.BooleanField()