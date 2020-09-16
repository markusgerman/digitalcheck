from django.shortcuts import render
import pandas as pd
from django.views.generic import TemplateView

from ..models.reportmodels import Digitalisierungsgrad

# Create your views here.

class ReportView(TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):

        grad = Digitalisierungsgrad()

        gradkmu = grad.berechneDigitalisierungsgrad("kmu")
        gradku = grad.berechneDigitalisierungsgrad("ku")

        context = {
            'gradkmu' : gradkmu,
            'gradku' : gradku,
        }

        return context
    
    