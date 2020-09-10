from django.shortcuts import render
from ..models.analyticmodels import FillAnalytics
from ..models.models import Core
from django.views.generic import TemplateView

class AnalyticsChartView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        umfrageteilnehmer = self.FillUmfrageteilnehmer()

        unternehmensgroese = self.FillUnternehmensgroese()
    
        context = {
            'umfrageteilnehmer' : umfrageteilnehmer,
            'unternehmensgroese' : unternehmensgroese,
        }

        return context
    
    def FillUmfrageteilnehmer(self):

        data = FillAnalytics()
        ihk_ku = data.getihkkutteilnehmer()

        ihk_kmu = data.getihkkmuteilnehmer()

        myconsult = data.getmyconsultteilnehmer()

        return "{}, {}, {}".format(myconsult, ihk_ku, ihk_kmu)

    def FillUnternehmensgroese(self):
        
        obj = FillAnalytics()

        fill = obj.getteilnehmernachgroese()

        return fill