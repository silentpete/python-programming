first_name = "john"
last_name = "smith"
full_name = f"{first_name} {last_name}"

print(full_name)
print(full_name.title())
print(f"Hello, {full_name.title()}!")

# formating a line
message = f"Good Morning, {full_name.title()}."
print(message)

# print tab
print("\tDear John...")

# print newline
print("this\nis\na\nnewline!")

print("this\n\tis\n\t\ta\n\t\t\tnewline!")

language = "python "
print("'"+language+"'")
# remove whitespace to the right when printing
print("'"+language.rstrip()+"'")

print("'"+language+"'")

# save it off if you want it that way
language = language.rstrip()
print("'"+language+"'")

# remove whitespace left with lstrip() method
# remove both sides with strip() method