#blog/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from . import views_cbv

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name = 'post_detail'),
    path('cbv/new/', views_cbv.post_new)
]
