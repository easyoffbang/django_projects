#blog/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail),
 #   path('^new/$', views.post_new, name='post_new'),
  #  path('^<\d+:id>/edit/$', views.post_detail, name='post_detail')   #int처럼 속성이 아닌 \d+가 올 수 있는가?
]

