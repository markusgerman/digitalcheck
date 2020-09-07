from django.shortcuts import render
from ..models import analyticmodels
from django.views.generic import TemplateView

class AnalyticsChartView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hello"] =  "hello" 
        return context
    
