from django.db import models
import urllib.request 
import os
from pathlib import Path
import xml.etree.ElementTree as et

# Create your models here.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


#Füllt das Dashboard 
class FillDashboard():

    kleinunternehmen = "https://www.digital-check.de/umfrage/export/export_ku.php"
    kleinundmittelunternehmen = "https://www.digital-check.de/umfrage/export/export_kmu.php"
    xmldirkmu = os.path.join(BASE_DIR, 'xml/kmu.xml')
    xmldirku = os.path.join(BASE_DIR, 'xml/ku.xml')

    #Holt sich die Anzahl an Umfrageteilnhmer
    def getallumfrageteilnehmer(self, ug):

        if ug == "ku":
            path = self.xmldirku
        if ug == "kmu":
            path = self.xmldirkmu

        xmlTree = et.parse(path)

        elemList = []

        counter = 0
        for elem in xmlTree.iter():
            elemList.append(elem.tag)
        
            if (elem.tag == "element"):
                counter = counter + 1

        return counter

    def getumfrageteilnehmerlastweek(self):
        
        counter = 2

        return counter

    def getumfragengesamt(self):

        

        return counter


class Data:

    kleinunternehmen = "https://www.digital-check.de/umfrage/export/export_ku.php"
    kleinundmittelunternehmen = "https://www.digital-check.de/umfrage/export/export_kmu.php"
    xmldirkmu = os.path.join(BASE_DIR, 'xml/kmu.xml')
    xmldirku = os.path.join(BASE_DIR, 'xml/ku.xml')

    def __init__(self):
        #Holt die XML aus dem Web und speichert die auf dem Webserver.
        #Achtung, das dauert scheiße lange und sollte jede 5 Minuten per CJ ausgeführt werden.
        urllib.request.urlretrieve(self.kleinundmittelunternehmen, self.xmldirkmu)
        urllib.request.urlretrieve(self.kleinunternehmen, self.xmldirku)
