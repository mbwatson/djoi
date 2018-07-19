from django.contrib import admin
from django.urls import path
import djoi.publications.views as publication_views
import djoi.authors.views as author_views

# app_name = 'djoi'

urlpatterns = [
    path('authors', author_views.authors, name='djoi.authors'),
    path('authors/<slug:author_slug>/', author_views.author, name='djoi.author'),

    path('publications', publication_views.publications, name='djoi.publications'),
]
