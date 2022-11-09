import json

class Actor:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def tojson():
        dic = {
            "first_name": self.firstname,
            "last_name": self.lastname
            }
        json_obj = json.dumps(dic)
        return json_obj


class Movie:
    def __init__(self, title, direc, year):
        self.title = title
        self.direc = direc
        self.year = year
        self.actors = []

    def addActor(fname, lname):
        # TODO check params validity
        self.actors.append(Actor(fname, lname))

    def asDict():
        movdict = {
            "title": self.title,
            "director": self.direc,
            "year": self.year,
            "actors": #list of dictionnaries ??
        }
