from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=16)
    views = models.IntegerField(default=0)