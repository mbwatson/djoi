from django.contrib import admin
from django.urls import path
import djoi.publications.views as publicationViews
import djoi.authors.views as authorViews

app_name = 'djoi'

urlpatterns = [
    path('authors', authorViews.index, name='authors'),
    path('authors/<slug:author_slug>/', authorViews.detail, name='author'),

    path('publications', publicationViews.publications, name='publications'),

]
