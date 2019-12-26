# can set default parameter values
def get_first_initial(name, force_upper=False):
  if force_upper:
    initial = name[0:1].upper()
  else:
    initial = name[0:1]

  return initial

first_name = input("what is your first name? ")

first_name_initial = get_first_initial(first_name)

print("your first name first initial is: " + first_name_initial)
