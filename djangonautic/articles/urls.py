from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list' ),
    path('<slug:slug>/', views.article_details, name='article_details')
]
