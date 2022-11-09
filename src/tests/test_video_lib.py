import sys

sys.path.append("/home/toto/RT0704/src/video")

from person import Person
from movie import Movie
from videolib import Videolib


# ---- setup -----------
owner = Person("Denis", "Brognart")

mov1 = Movie("The Matrix", "The Wachowskis", 1999)
mov2 = Movie("Alien", "Ridley Scott", 1979)

mov1.addActor("Keanu", "Reeves")
mov1.addActor("Laurence", "Fishburne")
mov1.addActor("Carrie-Anne", "Moss")

mov2.addActor("Tom", "Skeritt")
mov2.addActor("Sigourney", "Weaver")

vlib = Videolib()

vlib.addOwner(owner)

vlib.addMovie(mov1)
vlib.addMovie(mov2)

# ---- test 1 : toJson() et fromJson()

vlib_json = vlib.toJson()
vlib2 = Videolib()
vlib2.fromJson(vlib_json)
vlib2_json = vlib2.toJson()

if vlib_json == vlib2_json:
    print("TEST 1: OK")

# ---- test 2 : save/load

vlib.save("testsav.json")
vlib3 = Videolib()
vlib3.load("testsav.json")

if vlib_json == vlib3.toJson():
    print("TEST 2: OK SI TEST 1 OK")


