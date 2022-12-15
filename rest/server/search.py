import os

# utilitaries

def list_files(uri):
    files = os.listdir("/home/toto/RT0704/rest/" + uri + "/")
    ret = ""
    for f in files:
        ret += uri + "/"
        ret += f
        ret = ret[:-5] # remove the extension 
        ret += '\n'

    return ret



