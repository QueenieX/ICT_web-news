from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('search', views.search, name='url Search'),
]