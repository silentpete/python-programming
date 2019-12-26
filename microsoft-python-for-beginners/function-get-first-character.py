def get_first_initial(name):
  initial = name[0:1].upper()
  return initial

first_name = input("what is your first name? ")

first_name_initial = get_first_initial(first_name)

print("your first name initial is: " + first_name_initial)
