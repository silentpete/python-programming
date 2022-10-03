def make_pizza(size, *toppings):
    """Summarisse the pizza we are about to make."""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushroom", "green pepper", "extra cheese")
