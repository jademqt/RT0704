"""
    file formats.py
    functions to test for arguments formats
"""

import re


def is_valid_URI(arg):
    """
        test if arg is a valid uri eg api/xxx/xxx...
    """

    if re.match('api/(movies|persons|vlib)/(.+)', arg) is not None:
        return True

    return False


