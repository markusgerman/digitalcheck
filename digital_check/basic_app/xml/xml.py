# Die Klasse holt jede n Minuten die verschlüsselten XML Dateien aus folgenden Links:
# https://www.digital-check.de/umfrage/export/export_kmu.php
# https://www.digital-check.de/umfrage/export/export_ku.php
#

import urllib.request 
import os
from pathlib import Path
import sys
import requests


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

class XML():
    kleinunternehmen = "https://www.digital-check.de/umfrage/export/export_ku.php"
    kleinundmittelunternehmen = "https://www.digital-check.de/umfrage/export/export_kmu.php"

    xmldirkmu = os.path.join(BASE_DIR, 'xml/kmu.xml')
    xmldirku = os.path.join(BASE_DIR, 'xml/ku.xml')

    xmlkmuenc = os.path.join(BASE_DIR, 'xml/dekmu.xml')
    xmlkuenc = os.path.join(BASE_DIR, 'xml/deku.xml')

    def __init__(self):

        urllib.request.urlretrieve(self.kleinundmittelunternehmen, self.xmldirkmu)
        urllib.request.urlretrieve(self.kleinunternehmen, self.xmldirku)

        self.decode(self.xmldirkmu, self.xmlkmuenc)
        self.decode(self.xmldirku, self.xmlkuenc)

    def decode(self, auswertung, enc):

        with open(auswertung, 'r', encoding='unicode_escape') as file:
            data = file.read() 
        
        userdata = {"IV": "kj3840120938934785489329834j484", "value": data}
        resp = requests.post('https://www.digital-check.de/umfrage/export/decrypt.php', data=userdata, verify=True)

        f = open(enc, "w", encoding="utf-8")
        f.write(resp.text)
        f.close()

x = XML()