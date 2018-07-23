from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoi.urls')),
    path('djoi/', include('djoi.urls')),
]
