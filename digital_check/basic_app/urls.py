from django.urls import path
from .views import views

urlpatterns = [
    path('', views.home, name='register'),
    path('maps/', views.map_view, name='map'),
    path('test/', views.test_view, name='test'),
]