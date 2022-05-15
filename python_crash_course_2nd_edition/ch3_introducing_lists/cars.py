cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list")
print(cars)
print("\nHere is the sorted list")
print(sorted(cars, reverse=True))
print("\nHere is the list")
print(cars)

print("")
cars.reverse()
print("Reverse order")
print(cars)
print(f"the length of cars list is {len(cars)}")