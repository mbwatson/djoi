from django.contrib import admin
from django.urls import path
from . import views

# app_name = 'djoi'

urlpatterns = [
    path('authors', views.authors, name='djoi.authors'),
    path('authors/<slug:author_slug>/', views.author, name='djoi.author'),

    path('publications', views.publications, name='djoi.publications'),
]
