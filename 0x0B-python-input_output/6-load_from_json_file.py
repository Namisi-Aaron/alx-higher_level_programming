#!/usr/bin/python3
"""Contains the function load from json file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    my_str = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for characters in f:
            my_str += characters
    return json.loads(my_str)
