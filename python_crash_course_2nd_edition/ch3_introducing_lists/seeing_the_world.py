locations = ['italy', 'spain', 'romania', 'poland', 'argentina']

print("Original Order:")
print(locations)

print(f"\nSort the list\n{sorted(locations)}")

print("\nShould print original")
print(locations)

print(f"\nSort the list and reverse\n{sorted(locations, reverse=True)}")

print("\nShould print original")
print(locations)

print("\nReverse the order and print")
locations.reverse()
print(locations)

print("\nReverse the order and print (should be original)")
locations.reverse()
print(locations)

print("\nsort the list")
locations.sort()
print(locations)

print("\nsort and reverse")
locations.sort(reverse=True)
print(locations)