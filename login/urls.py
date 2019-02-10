from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('new_pw', views.new_pw, name='new_pw'),
    path('changepw', views.changepw, name='changepw'),

]
