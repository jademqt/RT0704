import os
import sys
from flask import Flask, request

sys.path.append("/home/toto/RT0704/src")
sys.path.append("/home/toto/RT0704/src/video")

from formats import *
from person import *
from movie import *
from vlib import *
from config import *

from http_methods_func import *


# load config
config = Config("/home/toto/RT0704/src/sv.conf")

# differentiate action based on HTTP method
methodParse = {
    "GET": func_get_test,
    "PUT": func_put_test,
    "POST": func_post_test,
    "DELETE": func_del_test
    }


# load video libs
vidlib_path_arr = []
vidlib_arr = []
for fpath in os.listdir(config.fields["json_folder"]):
    if os.path.isfile(fpath):
        vidlib_path_arr.append(fpath)

for path in vidlib_path_arr:
    vidlib_arr.append(Videolib().new_from_file(path))

print("[DEBUG] searching for libraries in " + config.fields["json_folder"])
print("video libraries found :")
for lib in vidlib_path_arr:
    print(lib)


app = Flask(__name__)

@app.route("/<path:uri>", methods=["GET", "POST", "PUT", "DELETE"])
def main_func(uri):
    ans = methodParse[request.method](uri)  

    return ans

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=config.fields["port"])
