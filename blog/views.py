from pathlib import Path

from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import BlogArticles


def blog_title(request):
    MY_BASE_DIR = Path(__file__).resolve().parent.parent
    print('This is my base dir:',MY_BASE_DIR)
    blogs = BlogArticles.objects.all()
    return render(request, '../templates/blog/titles.html', {'blogs': blogs})


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article=get_object_or_404(BlogArticles,id=article_id)
    return render(request, '../templates/blog/content.html', {'article': article, })
