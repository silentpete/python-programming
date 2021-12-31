number = input("please give me a number and I'll tell you if it is divisible by 10? ")
number = int(number)

if number % 10 == 0:
    print(f"Your number {number} is a multiple of 10!")
else:
    print(f"Your number {number} is not a multiple of 10!")
