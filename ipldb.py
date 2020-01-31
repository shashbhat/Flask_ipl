from pymongo import MongoClient

url = "mongodb+srv://shash:yk2zGXxFJCetmolx@cluster0-i6qpy.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(url)
db = client.internship
collection = db.ipl2020

def get_team_labels():
    
    LabelList = []
    for x in collection.find({},{"_id":0,"Label":1}):
        LabelList.append(x["Label"])
    return LabelList

def get_all_team_details():
 
    teamList = []
    for x in collection.find({}):
        teamList.append(x)
    return teamList

def get_all_players():
    collection = db.players
    players = []
    for x in collection.find({}):
        players.append(x)
    return players

def get_team_players(teamName):
    collection = db.players
    players = []
    for x in collection.find({"Label":teamName}):
        players.append(x)
    return players

def get_players_role_count_by_team(teamName):
    collection = db.players
    x = collection.aggregate([
        {"$match":{"Label":teamName}},
        {"$group":{"_id":"$Role","count":{"$sum":1}}},
        {"$project":{"role":"$_id","count":1,"_id":0}}
    ])
    return [i for i in x]   
def get_players_role_count_ipl():
    pass
# min, max, avg, total salary of the team
def get_stat_team(teamname):
    collection = db.players
    res = collection.aggregate([
        {"$match":{"Label":teamname}},
        {"$group":
            {
                "_id":"$Label",
                "total":{"$sum":"$Price"},
                "max":{"$max":"$Price"},
                "min":{"$min":"$Price"},
                "avg":{"$avg":"$Price"}
            }
        },
    ])
    return [i for i in res]
# min, max, avg, total salary of the ipl2020
def get_stat_ipl():
    collection = db.players
    res = collection.aggregate([
        {"$group":{"_id":"$Label","total":{"$sum":"$Price"},"max":{"$max":"$Price"},"min":{"$min":"$Price"},"avg":{"$avg":"$Price"}}},
    ])
    return [i for i in res]


def get_players_by_role_by_team(role,teamName):
    collection = db.players
    res = collection.find({"Role":role,"Label":teamName})
    return [ x for x in res]



def get_role_by_team(teamname, role):
    collection = db.players
    roles = [i for i in collection.find({"Label":teamname,"Role":role})]
    return roles
    