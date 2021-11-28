"""itproger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #для подключения папки со статичными файлами
from django.conf.urls.static import static #для подключения папки со статичными файлами

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #при переходе на гл. стр. подключется файл urls, относящийся к приложению main
    path('news/', include('news.urls')) #при переходе на страницу news подключется файл urls, относящийся к приложению news
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #для подключения папки со статичными файлами
