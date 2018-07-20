from django.contrib import admin
from django.urls import path
import djoi.publications.views as publicationViews
import djoi.authors.views as authorViews
import djoi.staff.views as staffViews

# app_name = 'djoi'

urlpatterns = [
    # path('authors', authorViews.authors, name='djoi.authors'),
    # path('authors/<slug:author_slug>/', authorViews.author, name='djoi.author'),

    path('publications', publicationViews.publications, name='djoi.publications'),

    path('staff', staffViews.index, name='staff.index'),
    path('staff/<slug:staff_slug>', staffViews.detail, name='djoi.staff.member'),
]
