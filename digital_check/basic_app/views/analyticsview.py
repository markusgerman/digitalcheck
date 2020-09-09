from django.shortcuts import render
from ..models.analyticmodels import FillAnalytics
from ..models.models import Core
from django.views.generic import TemplateView

class AnalyticsChartView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = FillAnalytics()
        ihk_ku = data.getihkkutteilnehmer()

        ihk_kmu = data.getihkkmuteilnehmer()

        myconsult = data.getmyconsultteilnehmer()

        context["data"] =  "{}, {}, {}".format(myconsult, ihk_ku, ihk_kmu)

        return context
    
