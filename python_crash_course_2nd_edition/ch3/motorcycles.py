motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change a element of a list
motorcycles[0] = "ducati"
print(motorcycles)

# add element to list
motorcycles.append('ktm')
print(motorcycles)

motorcycles = []

motorcycles.append("honda")
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.append("suzuki")
print(motorcycles)

# insert elements into a list
motorcycles.insert(1, "ktm")
print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles.append('yamaha')

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("===example use case 1===")
motorcycles = ['honda', "suzuki", 'bmw']
last_owned = motorcycles.pop()
print(f"The last motorcyle I owned was a {last_owned.upper()}.")

print("===example use case 2===")
motorcycles = ['honda', "suzuki", 'bmw']
last_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned was a {last_owned.title()}.")

# remove element by name
motorcycles = ['honda', 'ktm', 'bmw', 'ducati']
print(motorcycles)
motorcycles.remove("ktm")
print(motorcycles)

print("===example use case 3===")
motorcycles = ['honda', 'ktm', 'bmw', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n\t {too_expensive.title()} is too expensive for me!\n")