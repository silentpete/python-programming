prompt = "\nWhat is your age?"

asking_age = True
while asking_age:
    age = input(prompt)

    if age.isalpha():
        print("you gave a string, I'm done with you")
        break
    elif int(age) <= 3:
        print("your ticket is free")
    elif int(age) <= 12:
        print("your ticket is $10")
    else:
        print("your ticket is $15")
