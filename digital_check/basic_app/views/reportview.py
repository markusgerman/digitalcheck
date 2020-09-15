from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView

from ..models.reportmodels import Reports

# Create your views here.

class ReportView(TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):

        grad = Reports() 
        grad = grad.tester()
        
        context = {
            'grad' : grad,
        }

        return context
    
    