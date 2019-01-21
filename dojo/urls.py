from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<x>\d+)/$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    re_path(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
]

