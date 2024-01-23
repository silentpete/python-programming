#!/usr/bin/env python3
"""
Required Environment Variables
SOPS_AGE_KEY_FILE
SOPS_AGE_RECIPIENTS
"""


# Import Internal Libraries
import os
import json
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

def sops_update_a_keys_value(account_idx, account):
    """
    update a keys value
    sops has:
        --set value    set a specific key or branch in the input document. value must be a json encoded string. (edit mode only). eg. --set '["somekey"][0] {"somevalue":true}'
    """
    account_element = f"[\"accounts\"][{account_idx}]"
    updated_account_json = f"{json.dumps(account)}"
    try:
        print(f"sops --set '{account_element} {updated_account_json}' {file_path}")
        sops_command_response = os.system(f"sops --set '{account_element} {updated_account_json}' {file_path}")
        if sops_command_response != 0:
            print('sops did not return 0')
            print(f"returned: {sops_command_response}")
            sys.exit(1)
    except subprocess.CalledProcessError as ex:
        print(f"the exeption: {ex}")
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

for acct_idx, acct in enumerate(decrypted_contents_dict['accounts']):
    if acct['name'] == 'sa-a':
        acct['password'] = 'scriptAdjusted'
        print(acct_idx, acct)

        for token in acct['tokens']:
            if token['type'] == 'user_token':
                token['token'] = "scriptAdjusted"

        sops_update_a_keys_value(acct_idx, acct)
