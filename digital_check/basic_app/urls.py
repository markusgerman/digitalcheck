from django.urls import path
from .views import views
from .views import analyticsview

urlpatterns = [
    path('', views.home, name='register'),
    path('maps/', views.map_view, name='map'),
    path('test/', views.test_view, name='test'),
    path('analytics/', analyticsview.AnalyticsChartView.as_view(), name="analytics")
]