from django.urls import path
from .views import views
from .views import analyticsview
from .views import dashboardview

urlpatterns = [
    path('', dashboardview.home, name='register'),
    path('maps/', dashboardview.map_view, name='map'),
    path('analytics/', analyticsview.AnalyticsChartView.as_view(), name="analytics")
]