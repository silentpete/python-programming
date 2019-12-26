#!/usr/bin/env python

import yaml

yml_file = yaml.load(open('example.yaml'))

for p in yml_file['people']:
  print(p['firstname'])
