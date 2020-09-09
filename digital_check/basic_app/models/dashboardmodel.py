from django.db import models
from ..models.models import Core

import urllib.request 
import os
from pathlib import Path
import xml.etree.ElementTree as et

# Create your models here.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


#Füllt das Dashboard 
class FillDashboard():

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

