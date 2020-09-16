from ..models.models import Core, Dataframe, Liste
import pandas as pd

class Digitalisierungsgrad():

    def berechneKonstruktGewicht(self, ug, header):
        
        df = Dataframe()
        liste = Liste()

        if(ug == "kmu"):
            df = df.createpointFrameKMU()
            headers = liste.kmuliste()
        if(ug == "ku"):
            df = df.createpointFrameKU()
            headers = liste.kuliste()

        newheader = []

        for i in headers:
            if header in i:
                newheader.append(i)

        df["sum"] = df[newheader].sum(axis=1)

        listelements = len(newheader)

        df[header] = (100/(listelements * 3)) * df["sum"]

        return df[header]

    def berechneDigitalisierungsgrad(self, ug):

        if ug == "kmu":
            strategie = self.berechneKonstruktGewicht("kmu", "Strategie")
            struktur = self.berechneKonstruktGewicht("kmu", "Struktur")
            OrganisationaleKompetenzen = self.berechneKonstruktGewicht("kmu", "OrganisationaleKompetenzen")
            KulturWerte = self.berechneKonstruktGewicht("kmu", "KulturWerte")
            Mitarbeiterinnen = self.berechneKonstruktGewicht("kmu", "Mitarbeiterinnen")
            TechnologienITSysteme = self.berechneKonstruktGewicht("kmu", "TechnologienITSysteme")
            LieferantenprozesseSupplychain = self.berechneKonstruktGewicht("kmu", "LieferantenprozesseSupplychain")
            Kernprozesse = self.berechneKonstruktGewicht("kmu", "Kernprozesse")
            Kundenbeziehungsprozesse = self.berechneKonstruktGewicht("kmu", "Kundenbeziehungsprozesse")

            frames = [strategie, struktur, OrganisationaleKompetenzen, KulturWerte, Mitarbeiterinnen, TechnologienITSysteme, LieferantenprozesseSupplychain, Kernprozesse, Kundenbeziehungsprozesse]
        
        if ug =="ku":
            strategie = self.berechneKonstruktGewicht("ku", "Strategie")
            struktur = self.berechneKonstruktGewicht("ku", "Struktur")
            KulturWerte = self.berechneKonstruktGewicht("ku", "KulturWerte")
            Mitarbeiterinnen = self.berechneKonstruktGewicht("ku", "Mitarbeiterinnen")
            TechnologienITSysteme = self.berechneKonstruktGewicht("ku", "TechnologienITSysteme")
            LieferantenprozesseSupplychain = self.berechneKonstruktGewicht("ku", "LieferantenprozesseSupplychain")
            Kernprozesse = self.berechneKonstruktGewicht("ku", "Kernprozesse")
            Kundenbeziehungsprozesse = self.berechneKonstruktGewicht("ku", "Kundenbeziehungsprozesse")

            frames = [strategie, struktur, KulturWerte, Mitarbeiterinnen, TechnologienITSysteme, LieferantenprozesseSupplychain, Kernprozesse, Kundenbeziehungsprozesse]


        result = pd.concat(frames, axis=1, join='inner')

        result["sum"] = result.sum(axis = 1)

        result["reifegrad"] = result["sum"] / int(len(frames))

        digbeginner = 0
        digmithaltender = 0
        digvorreiter = 0

        for i in result["reifegrad"]:
            if i < 55:
                digbeginner += 1
            if i >= 55 and i < 75:
                digmithaltender += 1
            if i > 74:
                digvorreiter += 1


        return "{},{},{}".format(digbeginner, digmithaltender, digvorreiter)

        