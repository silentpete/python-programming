#!/usr/bin/env python3
"""
While writing a SonarQube API script, found that the payload being delivered is over URI and doesn't except json.
"""
import argparse
import random
import string

def generate_password(length: int):
    """
    generate_password is used to create a password of numeric, lower and upper
    case alphabetic characters, which also container at least one '-' or '_'.
    """
    characters = string.ascii_letters + string.digits + '-_'
    password = ''.join(random.choice(characters) for i in range(length))
    return password

parser = argparse.ArgumentParser()
parser.add_argument("--length", default=32, help="set length of characters in the password")
args = parser.parse_args()

# Generate and print a password
while True:
    PW = generate_password(int(args.length))
    if "-" in PW:
        print(PW)
        break
    elif "_" in PW:
        print(PW)
        break
