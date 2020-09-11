from django.db import models
from ..models.models import Core

import urllib.request 
import os
from pathlib import Path
import xml.etree.ElementTree as et
import datetime

# Create your models here.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


#Füllt das Dashboard 
class FillDashboard():

    def filldashboardumfragenmonat(self):
        dataframe = Core()

        kmu = dataframe.createdataframeKMU()
     
        x = kmu['submitdate']
        
        dt = datetime.datetime.today()
        
        m = str(dt.month)
        y = str(dt.year)

        string = y + "-" + "0" + m

        counter = 0
        for c in x:
            if string in c:
                counter += 1

        ku = dataframe.createdataframeKU()

        y = ku['submitdate']

        for d in y:
            if string in d:
                counter += 1

        context = {
            'umfragenM' : counter,
        }

        return context

    def filldashboardcounter(self):
        
        dataframe = Core()

        counterKMU = dataframe.createdataframeKMU()
        counterKMU = counterKMU.index
        kmu = len(counterKMU)

        counterKU = dataframe.createdataframeKU()
        counterKMU = counterKU.index
        ku = len(counterKU)

        umfragenGesamt = kmu + ku

        context = {
            'kmu' : kmu,
            'ku' : ku,
            'umfragenG': umfragenGesamt,
            #'umfragenM' : umfragenMonat,
        }

        return context

