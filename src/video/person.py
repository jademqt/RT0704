# Classe représentant une personne
class Person:
    # Constructeur
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    # Renvoie un dictionnaire représentant la classe
    def toDict(self):
        dic = {
            "first_name": self.firstname,
            "last_name": self.lastname
            }
        return dic


    # Initialise l'objet avec les valeurs contenues dans un dictionnaire
    # L'objet doit etre créé (pas un constructeur)
    def fromDict(self, dic):
        self.firstname = dic["first_name"]
        self.lastname = dic["last_name"]


    def as_json(self):
        #TODO
