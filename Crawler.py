from bs4 import BeautifulSoup
import json


class Crawler:

    def __init__(self, artistHtmlSource):
        self.artist = dict()
        self.artist["name"] = ""
        self.artist["albums"] = []
        self.artist["singles"] = []
        self.artist["similarArtists"] = []
        
        self.artistHtmlSource = artistHtmlSource
        self.soup = None
        
        self.albumsSection = None
        self.singlesSection = None
        self.similarArtistsSection = None
        
        with open(self.artistHtmlSource, "rb") as f:
            self.soup = BeautifulSoup(f, features="html.parser")

        self.artist["name"] = self.soup.find("h1", "gj6rSoF7K4FohS2DJDEm").string
    
    def setSections(self):
       # acha tags que contenha cabeçalho dos albuns/singles
        albumsSection = self.soup.find("h2", string="Albums")
        singlesSection = self.soup.find("h2", string="Singles and EPs")
        similarArtistsSection = self.soup.find("h2", string="Fans also like")

        # acha seção superior da tag cabeçalho
        albumsSectionParent = albumsSection.find_parent("div").find_parent("div")
        singlesSectionParent = singlesSection.find_parent("div").find_parent("div")
        similarArtistsSection = similarArtistsSection.find_parent("div").find_parent("div")

        # acha albuns/singles dentro da tag cabeçalho
        self.albumsSection = albumsSectionParent.find_all("a")
        self.singlesSection = singlesSectionParent.find_all("a")
        self.similarArtistsSection = similarArtistsSection.find_all("a")

    def extractMusicInfo(self, infoType):
        section = []
        
        if infoType == "similarArtists":
            section = self.similarArtistsSection
            
            for sect in section:
                data = dict()
                data["name"] = sect.find_all("span")[0].string                       # NAME
                self.artist[infoType].append(data)
            return
        
        elif infoType == "albums":
            section = self.albumsSection
        
        elif infoType == "singles":
            section = self.singlesSection
        
        #itera section e extrai informacoes dela
        for sect in section:
            data = dict()
        
            data["name"] = sect.find_all("span")[0].string                       # NAME
            data["img"] = sect.find_all("div")[0].find_all("img")[0]["src"]      # COVER
            data["year"] = sect.find_all("div")[1].string                        # [ TYPE o YEAR ]
            
            data["year"] = data["year"].split(" ")
            data["type"] = data["year"][0]
            data["year"] = data["year"][2]
            self.artist[infoType].append(data)
            
    def createJson(self):
        # escrever dados num .json
        fileName = self.artist["name"] + ".json"
        
        jsonStr = json.dumps(self.artist, indent=4, ensure_ascii=True)
        jsonFile = open(fileName, "w")
        jsonFile.write(jsonStr)
        jsonFile.close()



sourceFiles = ["gojira.html", "angra.html", "opeth.html", "bowie.html"]

for file in sourceFiles:
    craw = Crawler(file)
    craw.setSections()
    craw.extractMusicInfo("albums")
    craw.extractMusicInfo("singles")
    craw.extractMusicInfo("similarArtists")
    craw.createJson()
