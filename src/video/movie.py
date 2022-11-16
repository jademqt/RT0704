import json
from person import *

class Movie:
    """
        Class modeling a movie

        fields:
            director   (str): URI to a Person JSON file (api/persons/file_name)
            title    (str)
            year     (int)
            uri      (str): own URI
            actors  (list): List of URIs to Person JSON files

        note: I'm feeling tired, so if you REALLY need info on the following functions,
              please refer to the comments in the person.py file
    """

    def __init__(self, dire, titl, year, act, uri):
        self.director = dire #uri
        self.title = titl
        self.year = year
        self.actors = act #uris
        self.uri = uri #own uri


    def add_actor(self, act_uri):
        self.actors.append(act_uri)


    def setURI(self, uri):
        self.uri = uri


    def as_json(self):
        d = {
            "director": self.director,
            "title": self.title,
            "year": self.year,
            "actors": self.actors
        }

        return json.dumps(d)


    def from_json(self, json_object):
        d = json.loads(json_object)

        self.director = d["director"]
        self.title = d["title"]
        self.year = d["year"]
        self.actors = d["actors"]

    
    def load_file(self):
        with open(self.uri, "r") as f:
            d = json.load(f)

        self.director = d["director"]
        self.title = d["title"]
        self.year = d["year"]
        self.actors = d["actors"]


    def save(self):
        d = {
            "director": self.director,
            "title": self.title,
            "year": self.year,
            "actors": self.actors
        }

        with open(self.uri, "w") as f:
            json.dump(d, f)


    @classmethod
    def empty(cls):
        return Movie("", "", 0, "")


    @classmethod
    def new_from_file(cls, uri):
        with open(uri, "r") as f:
            d = json.load(f)

        return Movie(d["director"], d["title"],
                d["year"], d["actors"], uri)

    
    @classmethod
    def new_from_json(cls, json_object):
        d = json.loads(json_object)

        return Movie(d["director"], d["title"],
                d["year"], d["actors"], "")
