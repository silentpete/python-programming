#!/usr/bin/env python3

# Import Standard Libraries
import json

# Import External Libraries
import yaml

with open('dictionary.yaml', 'r', encoding="utf-8") as file:
    dictionary = yaml.safe_load(file)

print(json.dumps(dictionary))
