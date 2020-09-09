from django.db import models

from ..models.models import Core


class FillAnalytics():

    def getihkkutteilnehmer(self):

        dataframe = Core()

        dfku = dataframe.createdataframeKU()
        
        surveyids = dfku['SurveyID']
        
        counter = 0
        for c in surveyids:
            if c == "313385":
                counter += 1
            
    
        return counter

    def getihkkmuteilnehmer(self):

        dataframe = Core()

        dfkmu = dataframe.createdataframeKMU()

        surveyids = dfkmu['SurveyID']

        counter = 0
        for c in surveyids:
            if c == "645677" or c == "645677_Alt":
                counter += 1

        return counter

    def getmyconsultteilnehmer(self):

        dataframe = Core()

        dfku = dataframe.createdataframeKMU()

        surveyids = dfku['SurveyID']

        counter = 0
        for c in surveyids:
            if c == "942385":
                counter += 1
        
        return counter


    