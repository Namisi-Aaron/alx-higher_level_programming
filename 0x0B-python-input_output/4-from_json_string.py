#!/usr/bin/python3
"""from_json_string module"""
from json import json
def from_json_string(my_str):
    """from_json_string returns an object
    represented by a json string"""

    return json.loads(my_str)
