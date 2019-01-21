from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),

]
