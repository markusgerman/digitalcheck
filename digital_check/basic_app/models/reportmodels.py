from ..models.models import Core, Dataframe

class Reports():

    def tester(self):

        dig = Digitalisierungsgrad()
        return dig.Fragebogen1()


class Digitalisierungsgrad():

    kmuliste = ["StrategieSQ001","StrategieSQ002","StrategieSQ003", "StrategieSQ004", "StrategieSQ005", "StrategieSQ006",	"StrategieSQ007",	"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004",	"StrukturSQ005",	"StrukturSQ006",	"StrukturSQ007",	"OrganisationaleKompetenzenSQ001",	"OrganisationaleKompetenzenSQ002",	"OrganisationaleKompetenzenSQ003","OrganisationaleKompetenzenSQ004",	"OrganisationaleKompetenzenSQ005",	"OrganisationaleKompetenzenSQ006",	"KulturWerteSQ001"	,"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005",	"KulturWerteSQ006"	,"KulturWerteSQ007"	,"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005"	,"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008"	,"MitarbeiterinnenSQ009",	"TechnologienITSystemeSQ001"	,"TechnologienITSystemeSQ002"	,"TechnologienITSystemeSQ003"	,"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007",	"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002"	,"LieferantenprozesseSupplychainSQ003"	,"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"LieferantenprozesseSupplychainSQ007",	"KernprozesseSQ001"	,"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KernprozesseSQ007",	"KernprozesseSQ008",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]
    kuliste = [ "StrategieSQ001",	"StrategieSQ002",	"StrategieSQ003",	"StrategieSQ004",	"StrategieSQ005"	,"StrukturSQ001",	"StrukturSQ002",	"StrukturSQ003",	"StrukturSQ004"	,"StrukturSQ005",	"StrukturSQ006",	"KulturWerteSQ001",	"KulturWerteSQ002",	"KulturWerteSQ003"	,"KulturWerteSQ004"	,"KulturWerteSQ005"	,"KulturWerteSQ006",	"KulturWerteSQ007",	"KulturWerteSQ008",	"MitarbeiterinnenSQ001",	"MitarbeiterinnenSQ002",	"MitarbeiterinnenSQ003",	"MitarbeiterinnenSQ004",	"MitarbeiterinnenSQ005",	"MitarbeiterinnenSQ006",	"MitarbeiterinnenSQ007",	"MitarbeiterinnenSQ008",	"TechnologienITSystemeSQ001",	"TechnologienITSystemeSQ002",	"TechnologienITSystemeSQ003",	"TechnologienITSystemeSQ004",	"TechnologienITSystemeSQ005",	"TechnologienITSystemeSQ006",	"TechnologienITSystemeSQ007"	,"TechnologienITSystemeSQ008",	"TechnologienITSystemeSQ009",	"LieferantenprozesseSupplychainSQ001",	"LieferantenprozesseSupplychainSQ002",	"LieferantenprozesseSupplychainSQ003",	"LieferantenprozesseSupplychainSQ004",	"LieferantenprozesseSupplychainSQ005",	"LieferantenprozesseSupplychainSQ006",	"KernprozesseSQ001",	"KernprozesseSQ002",	"KernprozesseSQ003",	"KernprozesseSQ004",	"KernprozesseSQ005",	"KernprozesseSQ006",	"KundenbeziehungsprozesseSQ001",	"KundenbeziehungsprozesseSQ002",	"KundenbeziehungsprozesseSQ003",	"KundenbeziehungsprozesseSQ004",	"KundenbeziehungsprozesseSQ005",	"KundenbeziehungsprozesseSQ006",	"KundenbeziehungsprozesseSQ007"]
    
    def Strategie(self):
        
        df = Dataframe()
        df = df.createpointFrameKMU()

        df['Total'] = "StrategieSQ001","StrategieSQ002","StrategieSQ003", "StrategieSQ004", "StrategieSQ005", "StrategieSQ006",	"StrategieSQ007",

        pass
    

        