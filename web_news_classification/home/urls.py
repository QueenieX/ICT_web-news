from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('business', views.businessCategory, name='Business Category'),
    path('politics', views.politicsCategory, name='Politics Category'),
    path('entertainment', views.entertainmentCategory, name='Entertainment Category'),
    path('sport', views.sportCategory, name='Sport Category'),
    path('tech', views.techCategory, name='Tech Category'),
]