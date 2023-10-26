#!/usr/bin/env python3

ADDRESS = 'https://www.domain.com/'
print(ADDRESS)
print("trim ADDRESS")
ADDRESS = ADDRESS.rstrip('/')

print(ADDRESS)
print("run trim again")
ADDRESS = ADDRESS.rstrip('/')

print(ADDRESS)
