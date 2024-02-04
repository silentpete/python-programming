#!/usr/bin/env python3
'''
Blah
'''

ACCOUNTS = {
    'accounts': [
        {
            'name': 'sa-a',
            'login': 'sa-a',
            'email': 'sa-a@system.nomail',
            'password': 'something',
            'tokens': [
                {
                    'name': 'sa-a-user_token',
                    'type': 'user_token',
                    'token': 'foasngosandgoin'
                }
            ]
        },
        {
            'name': 'sa-b',
            'login': 'sa-b',
            'email': 'sa-b@system.nomail',
            'password': 'somethingElse',
            'tokens': [
                {
                    'name': 'sa-b-user_token',
                    'type': 'user_token',
                    'token': ''
                }
            ]
        }
    ]
}

# print(ACCOUNTS)
# print(ACCOUNTS.keys())
# print(len(ACCOUNTS['accounts']))
# print(ACCOUNTS['accounts'])
# print(ACCOUNTS['accounts'][0].keys())
# print(ACCOUNTS['accounts'][0].values())
# print(ACCOUNTS['accounts'][0].items())
# print(ACCOUNTS['accounts'][0].get('name'))
# print(ACCOUNTS["accounts"][0]["name"])
# print(id(ACCOUNTS["accounts"][0]["name"]))
