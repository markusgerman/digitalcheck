from django.db import models
import urllib.request 
from pathlib import Path
import os
import pandas as pd
import xml.etree.ElementTree as et

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Core Model: 

class Core():

    kmu = os.path.join(BASE_DIR, 'xml/dekmu.xml')
    ku = os.path.join(BASE_DIR, 'xml/deku.xml')

    #Erstellt das Dataframe für KMU und gibt dieses zurück
    def createdataframeKMU(self):
        
        path = self.kmu

        df_cols = self.elementlist("kmu")

        xtree = et.parse(path)
        xroot = xtree.getroot()
        rows = []
        
        for node in xroot: 
            res = []
            res.append(node.attrib.get(df_cols[0]))
            for el in df_cols[1:]: 
                if node is not None and node.find(el) is not None:
                    res.append(node.find(el).text)
                else: 
                    res.append(None)
            rows.append({df_cols[i]: res[i] 
                        for i, _ in enumerate(df_cols)})
        
        out_df = pd.DataFrame(rows, columns=df_cols)
        #out_df.to_excel("auswertung_kmu.xls", sheet_name="data")
        return out_df

    def createdataframeKU(self):
        path = self.ku

        df_cols = self.elementlist("ku")

        xtree = et.parse(path)
        xroot = xtree.getroot()
        rows = []
        
        for node in xroot: 
            res = []
            res.append(node.attrib.get(df_cols[0]))
            for el in df_cols[1:]: 
                if node is not None and node.find(el) is not None:
                    res.append(node.find(el).text)
                else: 
                    res.append(None)
            rows.append({df_cols[i]: res[i] 
                        for i, _ in enumerate(df_cols)})
        
        out_df = pd.DataFrame(rows, columns=df_cols)

        
        #out_df.to_excel("auswertung_ku.xls", sheet_name="data")

        return out_df

    def elementlist(self, unternehmensgroese):

        if unternehmensgroese == "kmu":
            path = self.kmu
        else:
            path = self.ku

        xmlTree = et.parse(path)

        elemList = []

        
        counter = 0
        for elem in xmlTree.iter():
            if (elem.tag == "element"):

                if counter == 1:
                    return elemList
                else:
                    counter = counter + 1
            elemList.append(elem.tag)

class Dataframe():

    dataframe = Core()
    kmu = dataframe.createdataframeKMU()
    ku = dataframe.createdataframeKU()

    def createpointFrameKMU(self):

        kmu = self.kmu[["StrategieSQ001","StrategieSQ002","StrategieSQ003", "StrategieSQ004", "StrategieSQ005", "StrategieSQ006",	"StrategieSQ007",	"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004",	"StrukturSQ005",	"StrukturSQ006",	"StrukturSQ007",	"OrganisationaleKompetenzenSQ001",	"OrganisationaleKompetenzenSQ002",	"OrganisationaleKompetenzenSQ003","OrganisationaleKompetenzenSQ004",	"OrganisationaleKompetenzenSQ005",	"OrganisationaleKompetenzenSQ006",	"KulturWerteSQ001"	,"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005",	"KulturWerteSQ006"	,"KulturWerteSQ007"	,"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005"	,"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008"	,"MitarbeiterinnenSQ009",	"TechnologienITSystemeSQ001"	,"TechnologienITSystemeSQ002"	,"TechnologienITSystemeSQ003"	,"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007",	"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002"	,"LieferantenprozesseSupplychainSQ003"	,"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"LieferantenprozesseSupplychainSQ007",	"KernprozesseSQ001"	,"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KernprozesseSQ007",	"KernprozesseSQ008",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]]

        liste = ["StrategieSQ001","StrategieSQ002","StrategieSQ003", "StrategieSQ004", "StrategieSQ005", "StrategieSQ006",	"StrategieSQ007",	"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004",	"StrukturSQ005",	"StrukturSQ006",	"StrukturSQ007",	"OrganisationaleKompetenzenSQ001",	"OrganisationaleKompetenzenSQ002",	"OrganisationaleKompetenzenSQ003","OrganisationaleKompetenzenSQ004",	"OrganisationaleKompetenzenSQ005",	"OrganisationaleKompetenzenSQ006",	"KulturWerteSQ001"	,"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005",	"KulturWerteSQ006"	,"KulturWerteSQ007"	,"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005"	,"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008"	,"MitarbeiterinnenSQ009",	"TechnologienITSystemeSQ001"	,"TechnologienITSystemeSQ002"	,"TechnologienITSystemeSQ003"	,"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007",	"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002"	,"LieferantenprozesseSupplychainSQ003"	,"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"LieferantenprozesseSupplychainSQ007",	"KernprozesseSQ001"	,"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KernprozesseSQ007",	"KernprozesseSQ008",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]


        #String in Punkte Umwandlung
        for i in liste:
            kmu.loc[kmu["{}".format(i)] == ("trifft eher nicht zu "), '{}'.format(i)] = 1

        for i in liste:
            kmu.loc[kmu["{}".format(i)] == ("trifft zu "), '{}'.format(i)] = 3
        
        for i in liste:
            kmu.loc[kmu["{}".format(i)] == ("trifft zu"), '{}'.format(i)] = 3

        for i in liste:
            kmu.loc[kmu["{}".format(i)] == ("trifft nicht zu "), '{}'.format(i)] = 0

        for i in liste:     
            kmu.loc[kmu["{}".format(i)] == ("trifft teilweise zu"), '{}'.format(i)] = 2
        
        for i in liste:     
            kmu.loc[kmu["{}".format(i)] == ("trifft teilweise zu "), '{}'.format(i)] = 2

        return kmu


    def createpointFrameKU(self):
    
        ku = self.ku[[ "StrategieSQ001",	"StrategieSQ002",	"StrategieSQ003",	"StrategieSQ004",	"StrategieSQ005"	,"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004"	,"StrukturSQ005",	"StrukturSQ006",	"KulturWerteSQ001",	"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005"	,"KulturWerteSQ006",	"KulturWerteSQ007",	"KulturWerteSQ008",	"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005",	"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008",	"TechnologienITSystemeSQ001",	"TechnologienITSystemeSQ002",	"TechnologienITSystemeSQ003",	"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007"	,"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002",	"LieferantenprozesseSupplychainSQ003",	"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"KernprozesseSQ001",	"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]]

        liste = [ "StrategieSQ001",	"StrategieSQ002",	"StrategieSQ003",	"StrategieSQ004",	"StrategieSQ005"	,"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004"	,"StrukturSQ005",	"StrukturSQ006",	"KulturWerteSQ001",	"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005"	,"KulturWerteSQ006",	"KulturWerteSQ007",	"KulturWerteSQ008",	"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005",	"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008",	"TechnologienITSystemeSQ001",	"TechnologienITSystemeSQ002",	"TechnologienITSystemeSQ003",	"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007"	,"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002",	"LieferantenprozesseSupplychainSQ003",	"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"KernprozesseSQ001",	"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]

         #String in Punkte Umwandlung
        for i in liste:
            ku.loc[ku["{}".format(i)] == ("trifft eher nicht zu"), '{}'.format(i)] = 1

        for i in liste:
            ku.loc[ku["{}".format(i)] == ("trifft zu"), '{}'.format(i)] = 3

        for i in liste:
            ku.loc[ku["{}".format(i)] == ("trifft nicht zu "), '{}'.format(i)] = 0

        for i in liste:     
            ku.loc[ku["{}".format(i)] == ("trifft teilweise zu"), '{}'.format(i)] = 2

        return ku


class Liste():

    def kmuliste(self):
        Dataframe = Core()
        df =  Dataframe.createdataframeKMU()
        liste = list(df.columns.values)

        return liste

    def kuliste(self):
        Dataframe = Core()
        df =  Dataframe.createdataframeKU()
        liste = list(df.columns.values)

        return liste




