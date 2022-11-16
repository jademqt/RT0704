import json

class Person:
    """
        Class modeling a person

        fields :
            firstname (str)
            lastname  (str)
            uri       (str): own URI
    """

    def __init__(self, fname, lname, uri):
        """
            Default constructor
        """

        self.firstname = fname
        self.lastname = lname
        
        self.uri = uri


    def setURI(self, uri):
        """
            Useless but there for prettier code
        """

        if (is_valid_URI(uri)):
            self.uri = uri


    def as_json(self):
        """
            Returns JSON description of the instance
        """

        d = {
            "firstname": self.firstname,
            "lastname": self.lastname
        }

        return json.dumps(d)


    def from_json(self, json_object):
        """
            Updates instance with values read from json object
        """

        d = json.loads(json_object)

        self.firstname = d["firstname"]
        self.lastname = d["lastname"]


    def save(self):
        """
            Writes JSON representation to the file specified in self.uri
        """

        d = {
            "firstname": self.firstname,
            "lastname": self.lastname
        }

        with open(self.uri, "w") as f:
            json.dump(f, d)


    def load_file(self):
        """
            Reads JSON file at self.uri
        """

        with open(self.uri, "r") as f:
            d = json.load(f)

        self.firstname = d["firstname"]
        self.lastname = d["lastname"]


    @classmethod
    def empty(cls):
        """
            Creates an empty Person (just like me, pls help)
        """

        return Person("", "", "")


    @classmethod
    def new_from_file(cls, uri):
        """
            Creates a new Person from a filed specified in uri
        """

        with open(uri, "r") as f:
            d = json.load(f)

        return Person(d["firstname"], d["lastname"], uri)


    @classmethod
    def new_from_json(cls, json_object):
        """
            Creates a new Person from a JSON object
        """

        d = json.loads(json_object)
    
        return Person(d["firstname"], d["lastname"], "")
