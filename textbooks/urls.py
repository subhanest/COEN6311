from django.contrib import admin
from django.urls import path,include
from textbooks import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('available_textbooks',views.available_textbooks, name='available_textbooks'),
    path('comp250/',views.COMP250,name='comp250'),
    path('ai101/',views.AI101,name='ai101'),
    path('ml202/',views.ML202,name= 'ml202'),
    path('comp312/',views.COMP312,name='comp312')
]