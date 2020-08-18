from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='register'),
    path('teilnehmer/', views.teilnehmerauswertung_view, name='teilnehmer')
]