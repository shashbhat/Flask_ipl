from pymongo import MongoClient

url = "mongodb+srv://shash:yk2zGXxFJCetmolx@cluster0-i6qpy.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.internship
collection = db.ipl2020

def get_team_names():
    teamNames = [x['team'] for x in collection.find({},{"_id":0,"team":1})]
    return teamNames

def get_team_labels():
    teamLabels = [x['label'] for x in collection.find({},{"_id":0, "label":1})]
    return teamLabels

def get_team_details():
    teamList = [x for x in collection.find({})
    return teamList

def get_all_players():
    collection = db.players
    players = [x for x in collection.find({})]
    return players

def get_team_players(teamName):
    collection = db.players
    players = [x['label'] for x in collection.find{("label":teamName)]
    return players

