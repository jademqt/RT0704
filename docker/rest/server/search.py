import os
import json
from formats import *

# utilitaries

def list_files(uri):
    files = os.listdir('/app/' + uri + "/")
    ret = ""
    for f in files:
        ret += uri + "/"
        ret += f
        ret = ret[:-5] # remove the extension 
        ret += '\n'

    return ret

def list_files_raw(uri):
    files = os.listdir('/app/' + uri + "/")
    res = []

    for f in files:
        res.append('/app/'  + uri + "/" + f)

    return res


# search functions

def search_general(query):
    person_files = list_files_raw("api/persons")
    movie_files = list_files_raw("api/movies")
    vlib_files = list_files_raw("api/vlib")

    res = []

    files = person_files + movie_files + vlib_files

    for f in files: 
        with open(f, "r") as jsf:
            jsonobj = json.load(jsf)
    
        if 'first_name' in jsonobj:
            if jsonobj['first_name'] == query or jsonobj['last_name'] == query:
                res.append(f[23:-5])

        if 'title' in jsonobj:
            if jsonobj['title'] == query:
                res.append(f[23:-5])

    st = ""

    for p in res:
        st += p + "\n"

    return st
