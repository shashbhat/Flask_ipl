
from flask import Flask, jsonify 
import ipldb as ipldb
from mongoflask import MongoJSONEncoder

app = Flask(__name__)
app.json_encoder = MongoJSONEncoder


@app.route('/')
def welcome():
    return jsonify({"message":"Hello World"})


@app.route('/ipl/team/names')
def team_names():
    names = ipldb.get_team_names()
    return jsonify({"Team Names":names})


@app.route('/ipl/team/labels')
def team_labels():
    labels = ipldb.get_team_labels()
    return jsonify({"Team Label":labels})


if __name__ == "__main__":
    app.run(host="192.168.137.245", port=5000, debug=True)