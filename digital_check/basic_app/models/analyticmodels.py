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

    def getteilnehmernachgroese(self):

        ku = self.getihkkutteilnehmer()

        dataframe = Core()

        df = dataframe.createdataframeKMU()

        dfcolumn = df['D1']

        small = 0
        mittel = 0
        groes = 0

        for c in dfcolumn:
            if c == " 20-49 Mitarbeiter*innen":
                small += 1
            if c == " 50-249 Mitarbeiter*innern":
                mittel +=1
            if c == " ab 250 Mitarbeiter*innern":
                groes += 1

        return "{}, {}, {}, {}".format(ku, small, mittel, groes)

class FillBranche():

    def gethandelsbrancheKMU(self):

        dataframe = Core()

        df = dataframe.createdataframeKMU()

        dfcolumn = df[['D2','D4']]

        dfcolumn = dfcolumn[df['D2'] == "Handel"]
        
        dups = dfcolumn.pivot_table(index = ["D4"], aggfunc='size')

        liste = dups.tolist()
    
        return liste

    def gethandelsbrancheKU(self):

        dataframe = Core()

        df = dataframe.createdataframeKU()

        dfcolumn = df[['D2','D4']]

        dfcolumn = dfcolumn[df['D2'] == "Handel"]

        dfcolumn = dfcolumn.pivot_table(index=['D4'], aggfunc='size')

        dic = dfcolumn.to_dict()

        return dic