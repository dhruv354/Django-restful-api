from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('article/', views.article_list, name='article-list'),
    path('article/<int:pk>/', views.article_detail, name='article-detail')
]
