"""
    file formats.py
    functions to test json formats
"""

import re
import json


def is_valid_uri(arg):
    """
        test if arg is a valid uri eg api/xxx/xxx...
    """

    if re.match('api/(movies|persons|vlib)', arg) is not None:
        parts = arg.split("/")

        if len(parts) <= 3: # reject uri if too long
            if parts[-1] != '': # reject uri if it ends with '/'
                return True

    return False


def is_person_uri(uri):
    if re.match('api/persons/(.+)', uri) is not None:
        return True
    return False


def is_movie_uri(uri):
    if re.match('api/movies/(.+)', uri) is not None:
        return True
    return False


def json_is_person(json_str):
    d = json.loads(json_str)

    if (len(d) != 3):
        return False

    if (('first_name' in d) and ('last_name' in d) and ('tag' in d)):
        return True

    return False


def json_is_movie(json_str):
    d = json.loads(json_str)

    if (len(d) != 4):
        return False

    if (('director' in d) and ('title' in d)):
        if (('year' in d) and ('actors' in d)):
            uris = d['actors']

            for a in uris:
                if (not is_person_uri(a)):
                    return False
            
            if (not is_person_uri(d['director'])):
                return False

            return True

    return False


def json_is_vlib(json_str):
    d = json.loads(json_str)

    if len(d) != 2:
        return False

    if (('owner' in d) and ('movies' in d)):
        mov = d['movies']

        for m in mov:
            if not is_movie_uri(m):
                return False

        if not is_person_uri(d['owner']):
            return False

        return True

    return False
