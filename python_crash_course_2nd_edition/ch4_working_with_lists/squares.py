# do each step
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# don't need the extra step of saving off the square
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

print("=== example of above with list comprehensions ===")
squares = [value**2 for value in range(1,11)]
print(squares)
