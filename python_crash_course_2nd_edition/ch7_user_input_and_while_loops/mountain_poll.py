responses = {}

# set a flag to indicate the polling is active
polling = True

while polling:
    # prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary
    responses[name] = response

    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person response? (yes/no) ")
    if 'n' in repeat.lower():
        polling = False

# polling is complete, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
