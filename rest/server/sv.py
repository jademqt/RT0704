import os
import sys
import json
from flask import Flask, request

from formats import *
from person import *
from movie import *
from vlib import *


def path_from_uri(uri, dotflag):
    path = config["server_root"] + "/" + uri
    if (dotflag):
        path += ".json"

    return path


def func_get_test(uri):
    return "test get uri = {}".format(uri)    

def func_put_test(uri):
    return "test put uri = {}".format(uri)

def func_post_test(uri):
    objtype = uri.split('/')[1]
    full_path = path_from_uri(uri, True)
   
    # No data
    if len(request.data) == 0:
        return "NOK"

    # File exists
    if (os.path.exists(full_path)):
        return "NOK"

    json_obj = request.get_json()

    # Check format
    if (objtype == 'persons'):
        if not dict_is_person(json_obj):
            return "NOK"
    elif (objtype == 'movies'):
        if not json_is_movie(json_obj):
            return "NOK"
    elif (objtype == 'vlib'):
        if not json_is_vlib(json_obj):
            return "NOK"

    print("[debug] received json object : ", json_obj)

    # Write to file
    with open(full_path, "w") as f:
        json.dump(json_obj, f)

    return "OK"

def func_del(uri):
    full_path = path_from_uri(uri, True)

    if (os.path.exists(full_path)):
        os.system("rm {}".format(full_path))
        return "OK"
    
    return "NOK"




# load config
with open("config.json", "r") as f:
    config = json.load(f)

# differentiate action based on HTTP method
methodParse = {
    "GET": func_get_test,
    "PUT": func_put_test,
    "POST": func_post_test,
    "DELETE": func_del
}


# load video libs
vidlib_path_arr = []
vidlib_arr = []
for fpath in os.listdir(config["path_vlib"]):
    if os.path.isfile(fpath):
        vidlib_path_arr.append(fpath)

for path in vidlib_path_arr:
    vidlib_arr.append(Videolib().new_from_file(path))

print("[DEBUG] searching for libraries in " + config["path_vlib"])
print("video libraries found :")
for lib in vidlib_path_arr:
    print(lib)


app = Flask(__name__)

@app.route("/<path:uri>", methods=["GET", "POST", "PUT", "DELETE"])
def main_func(uri):
    if not is_valid_uri(uri):
        return "NOK"

    ans = methodParse[request.method](uri)  

    return ans

if __name__ == "__main__":
    app.run(debug=True, host=config["address"], port=config["port"])
