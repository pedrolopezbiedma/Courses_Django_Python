from django.shortcuts import render
from .models import Article

def articles_list(request): 
    articles_list = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles_list': articles_list})
