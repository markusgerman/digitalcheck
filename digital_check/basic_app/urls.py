from django.urls import path
from .views import views, dashboardview, analyticsview, reportview


urlpatterns = [
    path('', dashboardview.home, name='register'),
    path('maps/', dashboardview.map_view, name='map'),
    path('analytics/', analyticsview.AnalyticsChartView.as_view(), name="analytics"),
    path('reports/', reportview.ReportView.as_view(), name="reports")
]