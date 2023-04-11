from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def home():
    try:
        return "<p>Hello, World!</p>"
        
    except Exception as e:
        error = dict()
        error["error"] = e
        return e

@app.route("/artist/<name>/")
def getArtistByName(name):
    try:
        fileName = "./artists/" + name + ".json"
        artist = open(fileName)
        artistFile = json.load(artist)
        return artistFile
    
    except Exception as e:
        return json.dumps(e)
    
@app.route("/artist/<name>/albums/")
def getAlbumsByArtistName(name):
    try:
        fileName = "./artists/" + name + ".json"
        artist = open(fileName)
        artistFile = json.load(artist)
        
        albums = dict()
        albums["albums"] = artistFile["albums"]
        return json.dumps(albums)
    
    except Exception as e:
        return json.dumps(e)

@app.route("/artist/<name>/singles/")
def getSinglesByArtistName(name):
    try:
        fileName = "./artists/" + name + ".json"
        artist = open(fileName)
        artistFile = json.load(artist)
        
        singles = dict()
        singles["singles"] = artistFile["singles"]
        return json.dumps(singles)
    
    except Exception as e:
        return json.dumps(e) 

@app.route("/artist/<name>/similar/")
def getSimilarArtistsByArtistName(name):
    try:
        fileName = "./artists/" + name + ".json"
        artist = open(fileName)
        artistFile = json.load(artist)
        
        similarArtists = dict()
        similarArtists["similarArtists"] = artistFile["similarArtists"]
        return json.dumps(similarArtists)
    
    except Exception as e:
        return json.dumps(e)

@app.route("/artist/<name>/url/")
def getUrlByArtistName(name):
    try:
        fileName = "./artists/" + name + ".json"
        artist = open(fileName)
        artistFile = json.load(artist)
        
        url = dict()
        url["URL"] = artistFile["URL"]
        return json.dumps(url)
    
    except Exception as e:
        return json.dumps(e)

app.run()