from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    content = RichTextField('正文')