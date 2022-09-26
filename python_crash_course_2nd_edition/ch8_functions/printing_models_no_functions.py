# start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# show unprinted_desings
print(f"contents of unprinted desings: {unprinted_designs}")

# simulate printing each desing, until none are left
# move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# display all completed models
print(f"\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# show there are no unprinted_desings
print(f"contents of unprinted desings: {unprinted_designs}")
