import json
from person import *

class Movie:
    def __init__(self, auth, titl, year, act, uri):
        self.author = auth #uri
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
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "actors": self.actors
        }

        return json.dumps(d)


    def from_json(self, json_object):
        d = json.loads(json_object)

        self.author = d["author"]
        self.title = d["title"]
        self.year = d["year"]
        self.actors = d["actors"]

    
    def load_file(self):
        with open(self.uri, "r") as f:
            d = json.load(f)

        self.author = d["author"]
        self.title = d["title"]
        self.year = d["year"]
        self.actors = d["actors"]


    def save(self):
        d = {
            "author": self.author,
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

        return Movie(d["author"], d["title"],
                d["year"], d["actors"], uri)

    
    @classmethod
    def new_from_json(cls, json_object):
        d = json.loads(json_object)

        return Movie(d["author"], d["title"],
                d["year"], d["actors"], "")
