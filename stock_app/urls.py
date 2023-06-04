from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('home/', views.home, name="home"),
#    path('home/', views.log, name="home"),

    path('result/', views.result, name="result"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('venderlogin/', views.venderlogin, name="venderlogin"),
    path('venderhome/', views.venderhome, name="venderhome"),
    path('search/',views.search,name='search'),
]