#blog/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]
