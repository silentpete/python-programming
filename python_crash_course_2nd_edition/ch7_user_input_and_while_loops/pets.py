# remove all instances of specific value from a list

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']

print(f"pets before: {pets}")

while 'cat' in pets:
    pets.remove('cat')

print(f"pets after: {pets}")
