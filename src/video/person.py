import json

class Person:
    def __init__(self, fname, lname, uri):
        self.firstname = fname
        self.lastname = lname
        self.uri = uri


    def setURI(self, uri):
        self.uri = uri


    def as_json(self):
        d = {
            "firstname": self.firstname,
            "lastname": self.lastname
        }

        return json.dumps(d)


    def from_json(self, json_object):
        d = json.loads(json_object)

        self.firstname = d["firstname"]
        self.lastname = d["lastname"]


    def save(self):
        d = {
            "firstname": self.firstname,
            "lastname": self.lastname
        }

        with open(self.uri, "w") as f:
            json.dump(f, d)


    def load_file(self):
        with open(self.uri, "r") as f:
            d = json.load(f)

        self.firstname = d["firstname"]
        self.lastname = d["lastname"]


    @classmethod
    def empty(cls):
        return Person("","", "")


    @classmethod
    def new_from_file(cls, uri):
        with open(uri, "r") as f:
            d = json.load(f)

        return Person(d["firstname"], d["lastname"], uri)


    @classmethod
    def new_from_json(cls, json_object):
        d = json.loads(json_object)
    
        return Person(d["firstname"], d["lastname"], "")
