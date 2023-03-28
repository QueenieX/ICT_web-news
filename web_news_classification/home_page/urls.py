from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home Page'),
    path('business', views.businessCategory, name='Business'),
    path('politics', views.politicsCategory, name='Politics'),
    path('entertainment', views.entertainmentCategory, name='Entertainment'),
    path('sport', views.sportCategory, name='Sport'),
    path('tech', views.techCategory, name='Tech'),
]