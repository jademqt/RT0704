import requests
import json

#load config
with open("/home/toto/RT0704/config.json", "r") as f:
    config = json.load(f)

rest_full_address = "http://" + config["rest_address"] + ":" + str(config["rest_port"]) + "/"


def get_persons_list():
    res = requests.get(rest_full_address + "api/persons")
    return bytes.decode(res.content).split()

def get_movies_list():
    res = requests.get(rest_full_address + "api/movies")
    return bytes.decode(res.content).split()

def get_vlib_list():
    res = requests.get(rest_full_address + "api/vlib")
    return bytes.decode(res.content).split()


def new_person(fname, lname):
    pdict = { "first_name" : fname, "last_name" : lname }

    return requests.post(rest_full_address + "api/persons/" + fname.lower(), json = pdict)

def get_person(target):
    return requests.get(rest_full_address + "api/persons/" + target)

def del_person(target):
    return requests.delete(rest_full_address + "api/persons/" + target)


def new_movie():
    #TODO
    pass

def get_movie(target):
    return requests.get(rest_full_api + "api/movies/" + target)

def del_movie(target):
    return requests.delete(rest_full_api + "api/movies/" + target)


def new_vlib():
    #TODO
    pass

def get_vlib(target):
    return requests.get(rest_full_api + "api/vlib/" + target)

def del_vlib(target):
    return requests.delete(rest_full_api + "api/vlib/" + target)


