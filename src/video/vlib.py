import json
from person import *
from movie import *

class Vlib:
    def __init__(self, owne, uri):
        self.owner = owne #uri
        self.uri = uri #own uri
        self.movies = [] #uris


    def add_movie(self, mov_uri):
        self.movies.append(mov_uri)


    def setURI(self, uri):
        self.uri = uri


    def as_json(self):
        d = {
            "owner": self.owner,
            "movies": self.movies
        }

        return json.dumps(d)


    def from_json(self, json_object):
        d = json.loads(json_object)

        self.owner = d["owner"]
        self.movies = d["movies"]


    def load_file(self):
        with open(self.uri, "r") as f:
            d = json.load(f)
            
        self.owner = d["owner"]
        self.movies = d["movies"]


    def save(self):
        d = {
            "owner": self.owner,
            "movies": self.movies
        }

        with open(self.uri, "w") as f:
            json.dump(d, f)


    @classmethod
    def empty(cls):
        return Vlib("", "")


    @classmethod
    def new_from_file(cls, uri):
        with open(uri, "r") as f:
            d = json.load(f)

        return Vlib(d["owner"], d["movies"])


    @classmethod
    def new_from_json(cls, json_object):
        d = json.loads(json_object)

        return Vlib(d["owner"], d["movies"])
