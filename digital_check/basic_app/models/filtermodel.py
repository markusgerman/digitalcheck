from ..models.models import Core

class Query():
    dataframe = Core()
    df = dataframe.createdataframeKU()
    dfkmu = dataframe.createdataframeKMU()

    def create(self, liste, liste2):
        stringbuilder = ""
        counter = 0  
        for i in liste:
            counter += 1

        counter2 = 0
        for i in liste:
            counter2 += 1
            if counter2 == counter:
                stringbuilder = stringbuilder + i
            else:
                stringbuilder = stringbuilder + i + " or "

        stringbuilder2 = ""
        counter = 0  
        for i in liste2:
            counter += 1

        counter2 = 0
        for i in liste2:
            counter2 += 1
            if counter2 == counter:
                stringbuilder2 = stringbuilder2 + i
            else:
                stringbuilder2 = stringbuilder2 + i + " or "
        
        if stringbuilder == "":
            stringbuilder = stringbuilder2
        if stringbuilder2 == "":
            stringbuilder = stringbuilder
        if stringbuilder2 != "" and stringbuilder != "":
            stringbuilder = stringbuilder +" and " + stringbuilder2

        try:
            x = self.dfkmu.query(stringbuilder)
            y = self.df.query(stringbuilder)
            
            index  = x.index
            indey = y.index
            rows = len(index) + len(indey)

            return x.to_html(classes=["table-bordered", "table-striped", "table-hover"])
            
        except:
            return ""

        

        