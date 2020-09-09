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

    









