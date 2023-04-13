from flask import Flask
import json
import pymongo
from bson.json_util import dumps, loads

app = Flask(__name__)

dbConnection = pymongo.MongoClient("mongodb+srv://exa844:hwQfmACAGrTOZFdC@cluster0.crpzagf.mongodb.net/test")
database = dbConnection["artists"]
collection = database["artists"]

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
    # try:
    artist = collection.find({"name": name})
    artist = dumps(list(artist), indent = 2)
    return artist
    
    # except Exception as e:
    #     return json.dumps(e)
    
@app.route("/artist/<name>/albums/")
def getAlbumsByArtistName(name):
    # try:
    artist = collection.find({"name": name}, {"albums":1,"_id":0})
    artist = dumps(list(artist), indent = 2)
    
    return json.dumps(artist)
    
    # except Exception as e:
    #     return json.dumps(e)

@app.route("/artist/<name>/singles/")
def getSinglesByArtistName(name):
    # try:
    artist = collection.find({"name": name}, {"singles":1,"_id":0})
    artist = dumps(list(artist), indent = 2)
    
    return json.dumps(artist)
    
    # except Exception as e:
    #     return json.dumps(e) 

@app.route("/artist/<name>/similar/")
def getSimilarArtistsByArtistName(name):
    # try:
    artist = collection.find({"name": name}, {"similarArtists":1,"_id":0})
    artist = dumps(list(artist), indent = 2)
    
    return json.dumps(artist)
    
    # except Exception as e:
    #     return json.dumps(e)

@app.route("/artist/<name>/url/")
def getUrlByArtistName(name):
    # try:
    artist = collection.find({"name": name}, {"URL":1,"_id":0})
    artist = dumps(list(artist), indent = 2)
   
    return json.dumps(artist)
    
    # except Exception as e:
    #     return json.dumps(e)

app.run()