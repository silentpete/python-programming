usernames = ['tito', 'mario', 'jorge','admin', 'tex', 'luca']
# usernames = []

if usernames:
    for un in usernames:
        if un == 'admin':
            print(f"Hello, {un.title()}! Would you like to see a status report")
        else:
            print(f"Hello, {un.title()}! Thank you for logging in.")
else:
    print('we need to find some users')

print("\n5-10, checking usernames")
current_users = ['tito', 'mario', 'jorge','admin', 'tex', 'luca']
new_users = ['juan', 'LUCa', 'mike']

current_users_lower = []
for cu in current_users:
    current_users_lower.append(cu.lower())

for nu in new_users:
    if nu.lower() in current_users_lower:
        print(f"sorry {nu}, username taken, you will have to enter a differnt name.")
    else:
        print(f"nice! username {nu} available.")

print("\n5-11, ordinal numbers")
numbers = list(range(1,10))
for n in numbers:
    if n == 1:
        print('1st')
    elif n == 2:
        print('2nd')
    elif n == 3:
        print('3rd')
    else:
        print(f'{n}th')
