def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# function with default value
def describe_pet_with_default(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# positional arguments example
describe_pet("hairy dog", "marley")
describe_pet("snake", "snape")

# keyword arguments example
describe_pet(animal_type="fish", pet_name="goldie")
describe_pet(pet_name="george", animal_type="monkey")

# same code, but we added a default, if using a default, any that don't have defaults have to move left in the order.
describe_pet_with_default("peter")
describe_pet_with_default("peter", "lion")
