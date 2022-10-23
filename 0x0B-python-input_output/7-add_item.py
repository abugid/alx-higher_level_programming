#!/usr/bin/python3
"""
Module 7-add_item
Contains function that adds and saves to Python obj to JSON file; loads objects
# run with ./7-add_item.py
#
# cat add_item.json ; echo ""
# expect output: []
#
# ./7-add_item.py some random args
# cat add_item.json ; echo ""
# expect output: ["some", "random", "args"]
"""
import json
import sys
saveJson = __import__('5-save_to_json_file').save_to_json_file
loadJson = __import__('6-load_from_json_file').load_from_json_file

try:
    a = loadJson("add_item.json")
except (json.JSONDecodeError, FileNotFoundError):
    a = []

for i in range(1, len(sys.argv)):
    a.append(sys.argv[i])
saveJson(a, "add_item.json")
