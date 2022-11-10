import os
from flask import Flask

sys.path.append("/home/toto/RT0704/src")

from video.person import Person
from video.movie import Movie
from video.videolib import Videolib
from config import Config

# load config
config = Config("/home/toto/RT0704/src/sv.conf")

# differentiate action based on HTTP method
methodParse = {
    "GET": func_get,
    "PUT": func_put,
    "POST": func_post,
    "DELETE": func_delete
    }

# load video libs
vidlib_path_arr = []
vidlib_arr = []
for path in os.listdir(config.get_json_folder()):
    if os.isfile(path):
        vidlib_path_arr.append(path)

for path in vidlib_path_arr:
    vidlib_arr.append(Videolib().load(path))

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


# GET HTTP method > return resource as json
def func_get(uri_tab):
    if uri_tab.len() == 1:
        return vidlib_arr[uri_tab[0]].as_json()
