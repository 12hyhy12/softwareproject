"""cube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import view

urlpatterns = [
    url('index', view.index),
    url('about', view.about),
    url('contact', view.contact),
    url('map', view.map),
    url('news_show1', view.news_show1),
    url('news_show2', view.news_show2),
    url('news_show3', view.news_show3),
    url('news_show4', view.news_show4),
    url('news_show5', view.news_show5),
    url('news_show6', view.news_show6),
    url('news', view.news),
    url('newk', view.news1),
    url('product', view.product),
    url('indek', view.indek),
    url('water', view.water),
    url('solve', view.solve),
    url('initState', view.initState)
]

urlpatterns += staticfiles_urlpatterns()

