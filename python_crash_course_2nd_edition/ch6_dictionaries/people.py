print("pg 112, 6-7")
# from pg 99 6-1
person = {}
person['first_name'] = 'john'
person['last_name'] = 'smith'
person['age'] = 42
person['city'] = 'detroit'
print(person)

# 6-7
people = {
    'person_1': {
        'first_name': 'john',
        'last_name': 'smith',
        'age': 42,
        'city': 'detroit',
    },
    'person_2': {
        'first_name': 'jane',
        'last_name': 'smith',
        'age': 24,
        'city': 'detroit',
    },
}

for p, p_info in people.items():
    print(f"{p} has the full name of '{p_info['first_name'].title()} {p_info['last_name'].title()}', age '{p_info['age']}' and lives in '{p_info['city'].title()}.'")
