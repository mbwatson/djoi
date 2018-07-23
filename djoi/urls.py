from django.contrib import admin
from django.urls import path

from . import views
import djoi.publications.views as publicationViews
import djoi.staff.views as staffViews

app_name = 'djoi'

urlpatterns = [
    path('', views.index, name='index'),
    path('publications', publicationViews.publications, name='publications'),
    path('staff', staffViews.index, name='staff'),
    path('staff/<slug:employee_slug>/', staffViews.detail, name='employee'),
]
