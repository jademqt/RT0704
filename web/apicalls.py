import requests
import json

#load config
with open("/home/toto/RT0704/config.json", "r") as f:
    config = json.load(f)

rest_full_address = "http://" + config["rest_address"] + ":" + str(config["rest_port"]) + "/"


# GET requests
# used to get info about entry

# expected answer : string as "uri1\nuri2\n..."
def get_persons_list():
    res = requests.get(rest_full_address + "api/persons")
    return bytes.decode(res.content).split('\n')[:-1]

def get_movies_list():
    res = requests.get(rest_full_address + "api/movies")
    return bytes.decode(res.content).split('\n')[:-1]

def get_vlib_list():
    res = requests.get(rest_full_address + "api/vlib")
    return bytes.decode(res.content).split('\n')[:-1]


# expected answer : json object
def get_person(uri):
    return requests.get(rest_full_address + uri)

def get_movie(uri):
    return requests.get(rest_full_address + uri)

def get_vlib(uri):
    return requests.get(rest_full_address + uri)

# expected answer : string
def descriptor(uri):
    cat = uri.split('/')[1]

    if cat == 'persons':
        jsobj = json.loads(get_person(uri).content.decode())
        return jsobj['first_name'] + " " + jsobj['last_name']
    if cat == 'movies':
        jsobj = json.loads(get_movie(uri).content.decode())
        return jsobj['title']
    if cat == 'vlib':
        jsobj = json.loads(get_vlib(uri).content.decode())
        return jsobj['title']

    return "NOK"

# search
# expected answer : string as "uri1\nuri2\n..."
def search(query):
    par = { "query": query }
    return requests.get(rest_full_address + "api/search", params=par)

# POST requests
# used to create an entry
# expected answer : OK / NOK

def new_person(fname, lname, tag):
    pdict = { "first_name" : fname, "last_name" : lname, 'tag' : tag }
    res = requests.post(rest_full_address + "api/persons/" + fname.lower() + "_" + lname.lower(), json = pdict)
    i = 0

    while res.content.decode() == "EXISTS":
        res = requests.post(rest_full_address + "api/persons/" + fname.lower() + "_" + lname.lower() + "_" + str(i), json = pdict)
        i += 1

    return res


def new_movie(title, direc, year, actors):
    dir_uri = "api/persons/" + direc
    act_uris = []

    for a in actors:
        act_uris.append("api/persons/" + a)

    mdict = { "title": title, "year": int(year), "director": dir_uri, "actors": act_uris }

<<<<<<< HEAD
    return requests.post(rest_full_address + "api/movies/" + title.lower(), json = mdict)
=======
    i = 0
    res = requests.post(rest_full_address + "api/movies/" + title.lower() + "_" + year, json = mdict)
    
    while res.content.decode() == "EXISTS":
        res = requests.post(rest_full_address + "api/movies/" + title.lower() + "_" + year + "_" + str(i), json = mdict)
        i += 1

    return res
>>>>>>> 9535ee04975058ba35fd33e5a2cb45601deb1510


def new_vlib(title, owner, movies):
    owner_uri = "api/persons/" + owner
    mov_uris = []
    for m in movies:
        mov_uris.append("api/movies/" + m)

    vdict = { "title": title, "owner": owner_uri, "movies": mov_uris }

    res = requests.post(rest_full_address + "api/vlib/" + title.lower(), json = vdict)
    i = 0

    while res.content.decode == "EXISTS":
        res = requests.post(rest_full_address + "api/vlib/" + title.lower() + "_" + str(i), json = vdict)
        i += 1

    return res


# DELETE requests
# used to delete an entry (duh)
# expected answer : OK / NOK

def del_person(target):
    return requests.delete(rest_full_address + "api/persons/" + target).content

def del_movie(target):
    return requests.delete(rest_full_address + "api/movies/" + target).content

def del_vlib(target):
    return requests.delete(rest_full_address + "api/vlib/" + target).content


# PUT requests
# used to modify and entry
# expected answer : OK / NOK

# def mod_person(????)

# def mod_movie(????)

# def mod_vlib(????)
