from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list' ),
    path('new/', views.new_article, name='new_article' ),
    path('<slug:slug>/', views.article_details, name='article_details')
]
