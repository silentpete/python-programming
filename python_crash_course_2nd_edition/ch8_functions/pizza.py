def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza("pine apple")
make_pizza('mushrooms','green peppers')

def make_pizza_2(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza_2("pine apple")
make_pizza_2('mushrooms','green peppers')
