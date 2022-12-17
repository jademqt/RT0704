import os
import sys
import json
from flask import Flask, request

from formats import *
from search import *

def path_from_uri(uri, dotflag):
    path = config["app_root"] + "/rest/" + uri
    if (dotflag):
        path += ".json"

    return path

def func_get(uri):
    path = path_from_uri(uri, False)
    
    # list uris
    if uri == "api/vlib" or uri == "api/persons" or uri == "api/movies":
       return list_files(uri) 

    # search query
    if uri == "api/search":
        query = request.args.get("query")

        res = search_general(query)

        return res

    # info about object

    path += '.json'

    if not os.path.exists(path):
        return "NOK"
  
    with open(path, "r") as f:
        obj = json.load(f)

    return obj

def func_put_test(uri):
    return "ptdr uri : {}".format(uri)    

def func_post(uri):
    objtype = uri.split('/')[1]
    full_path = path_from_uri(uri, True)

    # No data
    if len(request.data) == 0:
        return "NOK"

    # File exists
    if (os.path.exists(full_path)):
        return "EXISTS"

    json_obj = request.get_json(force=True)
    json_str = json.dumps(json_obj)

    # Check format
    if (objtype == 'persons'):
        if not json_is_person(json_str):
            return "NOK"
    elif (objtype == 'movies'):
        print("92")
        if not json_is_movie(json_str):
            print("izi")
            return "NOK"
    elif (objtype == 'vlib'):
        if not json_is_vlib(json_str):
            return "NOK"

    # Write to file
    with open(full_path, "w") as f:
        json.dump(json_obj, f)

    return "OK"

def func_del(uri):
    full_path = path_from_uri(uri, True)
    
    if (os.path.exists(full_path)):
        os.system("rm {}".format("\"" + full_path) + "\"")
        return "OK"
    
    return "NOK"


# load config
with open("/home/toto/RT0704/config.json", "r") as f:
    config = json.load(f)

# differentiate action based on HTTP method
methodParse = {
    "GET": func_get,
    "PUT": func_put_test,
    "POST": func_post,
    "DELETE": func_del
}


app = Flask(__name__)

@app.route("/<path:uri>", methods=["GET", "POST", "PUT", "DELETE"])
def main_func(uri):
    if not is_valid_uri(uri):
        return "NOK"

    ans = methodParse[request.method](uri)  

    return ans

if __name__ == "__main__":
    app.run(debug=True, host=config["rest_address"], port=config["rest_port"])
