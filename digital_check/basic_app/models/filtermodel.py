from ..models.models import Core

class Counter():

    dataframe = Core()
    df = dataframe.createdataframeKU()
    dfkmu = dataframe.createdataframeKMU()

    def countdienstleistung(self):
        counter = 0
        for c in self.df["D2"]:
            if c == "Dienstleistung ":
                counter += 1
        for c in self.dfkmu["D2"]:
            if c == "Dienstleistung ":
                counter += 1

        return counter

    def counthandel(self):
        counter = 0
        for c in self.df["D2"]:
            if c == "Handel":
                counter += 1
        for c in self.dfkmu["D2"]:
            if c == "Handel":
                counter += 1

        return counter

    def countprodugewerbe(self):
        counter = 0
        for c in self.df["D2"]:
            if c == "Produzierendes Gewerbe":
                counter += 1
        for c in self.dfkmu["D2"]:
            if c == "Produzierendes Gewerbe":
                counter += 1

        return counter

    def kleinunternehmen(self):
        counter = 0

        for c in self.dfkmu["D1"]:
            if c == " 20-49 Mitarbeiter*innen":
                counter += 1

        return counter
        
    def mittelunternehmen(self):
        counter = 0

        for c in self.dfkmu["D1"]:
            if c == " 50-249 Mitarbeiter*innern":
                counter += 1
        return counter

    def großunternehmen(self):
        counter = 0

        for c in self.dfkmu["D1"]:
            if c == " ab 250 Mitarbeiter*innern":
                counter += 1
        return counter

    def kleinunternehmenKU(self):
        counter = 0
        for c in self.df["element"]:
            counter += 1

        return counter

class Query():
    dataframe = Core()
    df = dataframe.createdataframeKU()
    dfkmu = dataframe.createdataframeKMU()

    def create(self, liste):

        stringbuilder = ""

        counter = 0  #3
        for i in liste:
            counter += 1

        counter2 = 0
        for i in liste:
            counter2 += 1
            if counter2 == counter:
                stringbuilder = stringbuilder + i
            else:
                stringbuilder = stringbuilder + i + " or "

        try:
            x = self.dfkmu.query(stringbuilder)
            x.to_excel("exceltest.xlsx")   
        except:
            return None
        

        




       