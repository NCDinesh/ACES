from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class news(models.Model):
    news_title=models.CharField(max_length=50)
    news_desc=HTMLField()
    news_slug=AutoSlugField(populate_from='news_title',unique=True,null=True,default=None)
    news_image=models.ImageField(null=True,blank=True, upload_to="images/", height_field=None, width_field=None, max_length=None)
# Create your models here.
