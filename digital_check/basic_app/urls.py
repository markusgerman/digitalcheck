from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='register'),
    path('maps/', views.map_view, name='map')
]