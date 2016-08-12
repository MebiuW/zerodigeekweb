from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class OnlineEditorModel(models.Model):
    content = RichTextField()
