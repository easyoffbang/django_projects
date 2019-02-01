#blog/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name = 'post_detail'),
]
