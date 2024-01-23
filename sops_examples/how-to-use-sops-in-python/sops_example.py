#!/usr/bin/env python3
"""
Required Environment Variables
SOPS_AGE_KEY_FILE
SOPS_AGE_RECIPIENTS
"""


# Import Internal Libraries
import os
import subprocess
import sys

# Import External Libraries
import yaml

def sops_decrypt_file(sops_encrpted_file_path: str) -> str:
    """
    This function is used to return the contents of an encrypted file.
    """
    try:
        sops_decrypted_contents = subprocess.check_output(["sops", "-d", sops_encrpted_file_path])
        return sops_decrypted_contents.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)


# Start
script_path = os.path.dirname(os.path.realpath(__file__))
file_path = script_path+"/accounts.enc.yaml"
decrypted_contents = sops_decrypt_file(file_path)
print(decrypted_contents)
print(type(decrypted_contents))
decrypted_contents_dict = yaml.safe_load(decrypted_contents)
print(decrypted_contents_dict)
print(type(decrypted_contents_dict))
for a in decrypted_contents_dict["accounts"]:
    print(a["name"])
