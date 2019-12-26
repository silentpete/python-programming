def get_first_initial(name, force_upper):
  if force_upper:
    initial = name[0:1].upper()
  else:
    initial = name[0:1]

  return initial

first_name = input("what is your first name? ")

first_name_initial = get_first_initial(
  # if you call the parameter by name, they do not have to be in any order and your code is easier to read.
  force_upper=True,
  name=first_name
  )

print("your first name first initial is: " + first_name_initial)
