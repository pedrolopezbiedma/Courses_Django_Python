from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage ),
    path('articles/', include('articles.urls')),
    path('about/', views.about )
]

urlpatterns += static(settings.STATIC_URL)