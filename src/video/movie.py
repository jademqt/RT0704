from person import Person

# Classe représentant un film
class Movie:
    # Constructeur
    def __init__(self, title, direc, year):
        self.title = title
        self.direc = direc
        self.year = year
        self.actors = []

    
    def addActor(self, fname, lname):
        # TODO check params validity
        self.actors.append(Person(fname, lname))


    # Renvoie un dictionnaire représentant la classe
    def toDict(self):
        actordictlist = []
        for actor in self.actors:
            actordictlist.append(actor.toDict())

        movdict = {
            "title": self.title,
            "director": self.direc,
            "year": self.year,
            "actors": actordictlist
        }

        return movdict


    # Initialise l'objet avec les valeurs contenues dans un dictionnaire
    # Attention l'objet doit etre créé avant
    def fromDict(self, dic):
        self.title = dic["title"]
        self.direc = dic["director"]
        self.year = dic["year"]
        
        for ac in dic["actors"]:
            self.addActor(ac["first_name"], ac["last_name"])



