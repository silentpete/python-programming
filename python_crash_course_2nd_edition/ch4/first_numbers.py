print("=== show how range doesn't print last number ===")
for value in range(1, 5):
    print(value)

print("=== print 1 - 5 (have to range to 6) ===")
for value in range(1, 6):
    print(value)

print("=== can pass range single value, it'll start at 0 ===")
for value in range(6):
    print(value)

numbers = list(range(4))
print(numbers)
