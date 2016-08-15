from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class ArticlesModel(models.Model):
    title = models.CharField(max_length=64)
    source_type = models.IntegerField(default=1) #0 自动 1 原创 2转发 3 授权转发 4 未授权
    content = RichTextField(config_name='awesome_ckeditor')
    author_name = models.CharField(default='佚名',max_length=16)
    create_time = models.DateTimeField()
    author_url = models.URLField()
    author_email = models.EmailField()
    page_views = models.IntegerField(default=0)
    cover_img = models.URLField(default= None)

