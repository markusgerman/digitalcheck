from django.shortcuts import render
from ..models.analyticmodels import FillAnalytics, FillBranche
from ..models.models import Core
from django.views.generic import TemplateView

class AnalyticsChartView(TemplateView):
    template_name = 'analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        umfrageteilnehmer = self.FillUmfrageteilnehmer()

        unternehmensgroese = self.FillUnternehmensgroese()

        branche = self.FillBrancheValues()

        dienstleistungen = self.FillBranche("dienstleistung")
        handel= self.FillBranche("handel")
        produgewerbe = self.FillBranche("produgewerbe")
    
        context = {
            'umfrageteilnehmer' : umfrageteilnehmer,
            'unternehmensgroese' : unternehmensgroese,
            'branche' : branche,
            'dienstleistungen' : dienstleistungen,
            'handel' : handel,
            'produ' : produgewerbe,
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

    def FillBrancheValues(self):

        obj = FillBranche()

        value = obj.getbranche()

        return value

    def FillBranche(self, branche):

        obj = FillBranche()

        value = obj.getbranchedienstleistung(branche)

        return value