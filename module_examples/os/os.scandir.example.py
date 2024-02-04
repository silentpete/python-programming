import os

with os.scandir('.') as dir:
    for entry in dir:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
