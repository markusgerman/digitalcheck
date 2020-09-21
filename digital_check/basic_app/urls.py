from django.urls import path
from .views import views, dashboardview, analyticsview, reportview, exportview,filterview


urlpatterns = [
    path('', dashboardview.home, name='register'),
    path('maps/', dashboardview.map_view, name='map'),
    path('analytics/', analyticsview.AnalyticsChartView.as_view(), name="analytics"),
    path('reports/', reportview.ReportView.as_view(), name="reports"),
    path('export/', exportview.ExportView.as_view(), name="exports"),
    path('filter/', filterview.filter_view, name="exports"),
    path('merge/', exportview.export_btn, name="expt_btn"),
]