name = input("Please enter your name: ")
print(f"Hello, {name.capitalize()}!")

# pass a prompt for multiline prompts
prompt = "\nIf you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name.capitalize()}!")
