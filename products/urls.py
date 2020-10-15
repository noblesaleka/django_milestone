from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import url
from django.views.static import serve

urlpatterns = [
    path('', views.all_products, name='products'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

