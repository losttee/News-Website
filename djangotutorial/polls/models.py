from django.db import models
from tinymce.models import HTMLField

from .helpers import *
from .custom_field import * 
from .define import *
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICES, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={'category_slug':self.slug})
    
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('news/images/article', filename)
    
class Article(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    images = models.ImageField(upload_to= get_file_path)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = TABLE_ARTICLE_SHOW

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("article", kwargs={'article_slug':self.slug})
    
class Feed(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = TABLE_FEED_SHOW

    def get_absolute_url(self):
        return reverse("feed", kwargs={'feed_slug':self.slug})
    
class ArticleViewHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewed_at']
    