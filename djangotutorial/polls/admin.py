from django.contrib import admin
from django.db import models
from .define import *


# Register your models here.
from .models import Category, Article, Feed, ArticleViewHistory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering') 
    #prepopulated_fields =  {'slug': ('name',)}

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS


    list_filter = ["is_homepage", "status", "layout"]
    search_fields = ["name"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status', 'ordering', 'special') 
    #prepopulated_fields =  {'slug': ('name',)}
    is_special = models.BooleanField(default=False)

    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

    list_filter = ["status", "special", "category"]
    search_fields = ["name"]

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name','status', 'ordering') 
    #prepopulated_fields =  {'slug': ('name',)}
    is_special = models.BooleanField(default=False)

    class Media:
        js = ADMIN_SRC_JS

    list_filter = ["status"]
    search_fields = ["name"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Feed, FeedAdmin)

admin.site.site_header = ADMIN_HEADER_NAME



class ArticleViewHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'viewed_at')
    list_filter = ('user', 'viewed_at')
    search_fields = ('article__name', 'user__username')

admin.site.register(ArticleViewHistory, ArticleViewHistoryAdmin)