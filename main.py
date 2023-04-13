from bson.json_util import dumps
import functions_framework
import pymongo
import json

@functions_framework.http
def hello_http(request):
    map = dict()

    dbConnection = pymongo.MongoClient("mongodb+srv://exa844:hwQfmACAGrTOZFdC@cluster0.crpzagf.mongodb.net/test")
    database = dbConnection["artists"]
    collection = database["artists"]

    # /hello_http/artist?name=<name>&option=<option>

    if request.args.get('name') != '' and request.args.get('option') == "":
        try:
            name = request.args.get('name')
            artist = collection.find({"name": name})
            artist = dumps(list(artist), indent = 2)

            map["result"] = artist

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))


    elif request.args.get('name') != '' and request.args.get('option') == "albums":
        try:
            name = request.args.get('name')
            artist = collection.find({"name": name}, {"albums":1,"_id":0})
            artist = dumps(list(artist), indent = 2)

            map["result"] = artist

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    elif request.args.get('name') != '' and request.args.get('option') == "singles":
        try:
            name = request.args.get('name')
            artist = collection.find({"name": name}, {"singles":1,"_id":0})
            artist = dumps(list(artist), indent = 2)

            map["result"] = artist

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    elif request.args.get('name') != '' and request.args.get('option') == "similar":
        try:
            name = request.args.get('name')
            artist = collection.find({"name": name}, {"similarArtists":1,"_id":0})
            artist = dumps(list(artist), indent = 2)

            map["result"] = artist

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    elif request.args.get('name') != '' and request.args.get('option') == "url":
        try:
            name = request.args.get('name')
            artist = collection.find({"name": name}, {"URL":1,"_id":0})
            artist = dumps(list(artist), indent = 2)

            map["result"] = artist

        except Exception as e:
            map["message"] = 'Error: {}'.format(str(e))

    else:
        map["message"] = "name missing or with wrong value!"

    return json.dumps(map)