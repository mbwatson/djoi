from django.contrib import admin
from django.urls import path

from . import views

app_name = 'djoi'

urlpatterns = [
    path('', views.index, name='index'),
    path('publications/', views.publicationList, name='publications'),
    path('staff/', views.staffList, name='staff'),
    path('staff/<slug:employee_slug>/', views.staffDetail, name='employee'),
]
