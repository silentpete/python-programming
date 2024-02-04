#!/usr/bin/env python3

file_contents_dict = dict()
initial = 10

import yaml

with open('number.yaml', 'r', encoding="utf-8") as number_file:
    file_contents_dict = yaml.safe_load(number_file)

print(file_contents_dict["number"])
file_contents_dict["number"] = int(file_contents_dict["number"]) + int(initial)

print(yaml.dump(file_contents_dict))

with open('number.yaml', 'w') as number_file:
    number_file.write(yaml.dump(file_contents_dict))
