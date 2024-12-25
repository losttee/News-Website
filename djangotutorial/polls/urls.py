from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("category/<slug:category_slug>", views.category, name="category"),

    path("article/<slug:article_slug>", views.article, name="article"),

    path("feed/<slug:feed_slug>", views.feed, name="feed"),

    path("search", views.search, name="search"),
    
    path('tinymce/', include('tinymce.urls')), 

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('view_history/', views.view_history, name='view_history'),
    
]   

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)