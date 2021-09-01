from django.conf.urls.static import static
from django.urls.conf import include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from . import views
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_views.articles_list, name='home' ),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about )
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)