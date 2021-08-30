from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

def articles_list(request): 
    articles_list = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles_list': articles_list})

def article_details(request, slug): 
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', { 'article': article })

@login_required(login_url='accounts:login')
def new_article(request):
    if request.method == 'GET':
        form = forms.CreateArticle()
        return render(request, 'articles/new_article.html', {'form': form })

    else:
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            # Save form into DB
            return redirect('articles:articles_list')