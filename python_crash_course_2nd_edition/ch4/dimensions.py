dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tuples can't be assigned, the following will error
#dimensions[0] = 250

print("\nOriginal Dimensions")
for dimension in dimensions:
    print(dimension)

print("\nModified Demensions")
dimensions = (123, 456)
for dimension in dimensions:
    print(dimension)
