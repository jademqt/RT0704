import json

from person import Person
from movie import Movie


# Classe représentant une vidéothèque
class Videolib:
    # Constructeur
    def __init__(self):
        self.movies = []

    def addOwner(self, owner):
        self.owner = owner

    def addMovie(self, movie):
        self.movies.append(movie)

    
    # Renvoie une chaine de caractère correspondant à la sérialisation JSON de l'objet
    def toJson(self):
        moviesdictlist = []
    
        for mov in self.movies:
            moviesdictlist.append(mov.toDict())

        dic = {
            "owner": self.owner.toDict(),
            "movies": moviesdictlist
        }

        json_obj = json.dumps(dic)

        return json_obj


    # Désérialise une chaine de caractere JSON
    def fromJson(self, jsonobj):
        dic = json.loads(jsonobj)

        self.addOwner(Person("e", "e"))
        self.owner.fromDict(dic["owner"])

        for mov in dic["movies"]:
            m = Movie("e", "e", 0)
            m.fromDict(mov)
            self.addMovie(m)
        

    # Sauvegarde une vidéothèque sous la forme d'un fichier JSON
    def save(self, filename):
        json_obj = self.toJson()

        with open(filename, "w") as writefile:
            json.dump(json_obj, writefile)

    
    # Initialise une vidéothèque à partir d'un fichier JSON
    def load(self, filename):
        with open(filename, "r") as readfile:
            json_obj = json.load(readfile)

        self.fromJson(json_obj)

