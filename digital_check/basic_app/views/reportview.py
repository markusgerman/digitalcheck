from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView

from ..models.reportmodels import Digitalisierungsgrad

# Create your views here.

class ReportView(TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):

        grad = Digitalisierungsgrad()

        grad = grad.berechneDigitalisierungsgrad()
        
        context = {
            'grad' : grad,
        }

        return context
    
    