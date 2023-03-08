from bs4 import BeautifulSoup
import json

artist = dict()

# abrir discographySource.html e decodificar com o bs4
with open("source.html", "rb") as f:
    soup = BeautifulSoup(f, features="html.parser")

# achar tags que contenha cabeçalho dos albuns/singles
discographyHeader = soup.find("h2", string="Albums")
artist["name"] = soup.find("h1", "gj6rSoF7K4FohS2DJDEm").string
artist["albums"] = []

# achar seção superior da tag cabeçalho
albumsSection = discographyHeader.find_parent("div").find_parent("div")

# achar albuns dentro da tag cabeçalho
albums = albumsSection.find_all("a")

# iterar albuns e extrair info
for a in albums:
    album_data = dict()
    
    album_data["name"] = a.find_all("span")[0].string                       # ALBUM NAME
    album_data["img"] = a.find_all("div")[0].find_all("img")[0]["src"]      # ALBUM COVER
    album_data["year"] = a.find_all("div")[1].string                        # [ ALBUM o YEAR ]
    
    album_data["year"] = album_data["year"].split(" ")
    album_data["type"] = album_data["year"][0]
    album_data["year"] = album_data["year"][2]
    artist["albums"].append(album_data)
    
    # print(album_data, "\n")

jsonStr = json.dumps(artist, indent=4, ensure_ascii=True)
jsonFile = open("artists.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()

# escrever dados num .json