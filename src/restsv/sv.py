import os
import sys
from flask import Flask

sys.path.append("/home/toto/RT0704/src")
sys.path.append("/home/toto/RT0704/src/video")

from person import Person
from movie import Movie
from videolib import Videolib
from config import Config


# GET HTTP method > return resource as json
def func_get(uri_tab):
    if uri_tab.len() == 1:
        return vidlib_arr[uri_tab[0]].as_json()


# PUT HTTP method >
def func_put(uri_tab):
    #TODO
    pass


# POST HTTP method >
def func_post(uri_tab):
    #TODO
    pass


# DELETE HTTP method >
def func_del(uri_tab):
    #TODO
    pass



# load config
config = Config("/home/toto/RT0704/src/sv.conf")

# differentiate action based on HTTP method
methodParse = {
    "GET": func_get,
    "PUT": func_put,
    "POST": func_post,
    "DELETE": func_del
    }

# load video libs
vidlib_path_arr = []
vidlib_arr = []
for fpath in os.listdir(config.get_json_folder()):
    print("hmm " + fpath)
    if os.path.isfile(fpath):
        print("euh " + fpath)
        vidlib_path_arr.append(fpath)

for path in vidlib_path_arr:
    vidlib_arr.append(Videolib().load(path))

print("[DEBUG] searching for libraries in " + config.get_json_folder())
print("video libraries found :")
for lib in vidlib_path_arr:
    print(lib)

app = Flask(__name__)

@app.route("/<path:lien>", methods=["GET", "POST", "PUT", "DELETE"])
def main_func():
    # tableau contenant les champs de l'uri
    # [0] : library number
    # [1] : owner / movie number
    # [2] : if movie; actor number
    uri_tab = lien.split('/')

    ans = methodParse[request.method](uri_tab)  

    return ans


