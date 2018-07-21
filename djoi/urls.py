from django.contrib import admin
from django.urls import path
import djoi.publications.views as publicationViews
import djoi.authors.views as authorViews
import djoi.staff.views as staffViews

app_name = 'djoi'

urlpatterns = [
    path('authors', authorViews.index, name='authors'),
    path('authors/<slug:author_slug>/', authorViews.detail, name='author'),

    path('publications', publicationViews.publications, name='publications'),

    path('staff', staffViews.index, name='staff'),
    path('staff/<slug:employee_slug>/', staffViews.detail, name='employee'),
]
