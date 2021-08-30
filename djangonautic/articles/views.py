from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article

def articles_list(request): 
    articles_list = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles_list': articles_list})

def article_details(request, slug): 
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', { 'article': article })
