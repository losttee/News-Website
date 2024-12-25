from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse

from django.utils import timezone

from .models import Category, Article, Feed
import re
import feedparser
import json
from bs4 import BeautifulSoup
from .define import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleViewHistory

from django.shortcuts import render

from django.db.models import Max



def category(request, category_slug):
    #category_slug => thông tin category => article thuộc category => đổ dữ liệu ra phía client

    item_category = get_object_or_404(Category, slug = category_slug, status = APP_VALUE_STATUS_ACTIVE)

    items_article = Article.objects.filter(category = item_category, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)

    page = request.GET.get('page')

    items_article = paginator.get_page(page)

    return render(request, 'pages/category.html', {
        "title_page": item_category.name,
        "item_category": item_category,
        "items_article": items_article,
        "paginator" : paginator
    })

def article(request, article_slug):
    item_article = get_object_or_404(Article, slug = article_slug, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now())

     # Lưu lịch sử xem nếu người dùng đã đăng nhập
    if request.user.is_authenticated:
        ArticleViewHistory.objects.create(user=request.user, article=item_article)


    items_article_related = Article.objects.filter(category = item_article.category, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date').exclude(slug=article_slug)[:SETTING_ARTICLE_TOTAL_ITEMS_RELATED]

    return render(request, 'pages/article.html', {
        "title_page": item_article.name,
        "item_article": item_article,
        "items_article_related": items_article_related
    })

def feed(request, feed_slug):
    item_feed = get_object_or_404(Feed, slug = feed_slug, status = APP_VALUE_STATUS_ACTIVE)

    items_feed = []

    try:
        feed = feedparser.parse(item_feed.link)

        for entry in feed.entries:
            soup = BeautifulSoup(entry.summary, 'html.parser')
            img_tag = soup.find('img')
            src_img = '/media/news/images/feed/no-image1.png'

            if img_tag:
                src_img = img_tag['src']

            item = {
                'title': entry.title,
                'link': entry.link,
                'pub_date': entry.published,
                'img': src_img
            }

            items_feed.append(item)
    except:
        print("Get Feed: Error!")

    return render(request, 'pages/feed.html', {
        "title_page": item_feed.name,
        'items_feed': items_feed,
        'item_feed': item_feed
    })

def index(request):
    items_article_special = Article.objects.filter(special=True, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]

    items_category = Category.objects.filter(status=APP_VALUE_STATUS_ACTIVE, is_homepage=True).order_by('ordering')

    for category in items_category:
        category.article_filter = category.article_set.filter(status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    return render(request, 'pages/index.html', {
        "title_page": "Trang chủ",
        "items_article_special": items_article_special,
        "items_category": items_category
    })

def search(request):
    keyword = request.GET.get('keyword')

    items_article = Article.objects.filter(name__iregex=re.escape(keyword), status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)

    page = request.GET.get('page')

    items_article = paginator.get_page(page)

    return render(request, 'pages/search.html', {
        "title_page": "Tìm Kiếm Cho Từ Khóa: " + keyword,
        "items_article": items_article,
        "keyword": keyword,
        "paginator" : paginator
    })

# View đăng ký người dùng
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View đăng nhập người dùng
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# View đăng xuất người dùng
def user_logout(request):
    logout(request)
    return redirect('index')


def view_history(request):
    # Lấy danh sách bài viết đã xem, chỉ giữ lại bài viết gần nhất
    history = (
        ArticleViewHistory.objects.filter(user=request.user)
        .values('article')
        .annotate(latest_viewed_at=Max('viewed_at'))
        .order_by('-latest_viewed_at')
    )
    
    # Lấy các bài viết từ lịch sử đã xử lý
    article_ids = [item['article'] for item in history]
    articles = list(Article.objects.filter(id__in=article_ids))
    
    # Sắp xếp lại các bài viết theo thứ tự trong danh sách history
    article_map = {article.id: article for article in articles}
    sorted_articles = [article_map[article_id] for article_id in article_ids]

    # Phân trang
    paginator = Paginator(sorted_articles, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get('page')
    items_article = paginator.get_page(page)

    return render(request, 'pages/view_history.html', {
        'title_page': "Lịch Sử Đã Xem",
        'items_article': items_article,
        "paginator": paginator,
    })

