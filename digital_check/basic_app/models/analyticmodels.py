from django.db import models

from ..models.models import Core

import pandas as pd

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
            if c == "942385" or "942385_Alt":
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

    def getbranche(self):

        dataframe = Core()

        ku = dataframe.createdataframeKU()
        kmu = dataframe.createdataframeKMU()
        
        dienstleistung = 0
        produ = 0
        handel = 0

        ku = ku['D2']
        kmu = kmu['D2']

        for c in ku:
            if c == "Handel":
                handel += 1
            if c == "Produzierendes Gewerbe":
                produ += 1
            if c == "Dienstleistung ":
                dienstleistung += 1

        for c in kmu:
            if c == "Handel":
                handel += 1
            if c == "Produzierendes Gewerbe":
                produ += 1
            if c == "Dienstleistung ":
                dienstleistung += 1

        return "{}, {}, {}".format(dienstleistung, produ, handel)

    def getbranchedienstleistung(self, branche):

        dataframe = Core()

        df = dataframe.createdataframeKU()
        dfk = dataframe.createdataframeKMU()

        if branche == "dienstleistung": 
            pivot = df.pivot_table(index=['D3'], aggfunc='size')
            pivot2 = dfk.pivot_table(index=['D3'], aggfunc='size')
        if branche == "handel":
            pivot = df.pivot_table(index=['D4'], aggfunc='size')
            pivot2 = dfk.pivot_table(index=['D4'], aggfunc='size')
        if branche == "produgewerbe":
            pivot = df.pivot_table(index=['D5'], aggfunc='size')
            pivot2 = dfk.pivot_table(index=['D5'], aggfunc='size')


        dfs = [pivot, pivot2]
       
        dfs = pd.concat(dfs, axis=1)

        ende = dfs.append(dfs.sum().rename('Total')).assign(Total=lambda d: d.sum(1))

        ende = ende["Total"]

        names = ende.to_json(orient='index')

        return names

