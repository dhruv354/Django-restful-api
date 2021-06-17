from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('article/', views.article_api_view.as_view(), name='article-list'),
    path('article/<int:id>/', views.article_details_api_view.as_view(), name='article-detail'),
    path('generic/article/', views.GenericApiView.as_view()),
]
