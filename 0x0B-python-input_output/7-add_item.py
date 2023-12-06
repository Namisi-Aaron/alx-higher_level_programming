#!/usr/bin/python3
from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file
file_name = 'add_item.json'
if not os.path.isfile(file_name):
    myList = []
else:
    myList = load_from_json_file(file_name)
for i in range(1, len(argv)):
        myList.append(argv[i])
save_to_json_file(myList, file_name)
