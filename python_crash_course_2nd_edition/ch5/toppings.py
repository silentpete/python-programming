requested_topping = 'mushroom'
if requested_topping != 'anchovies':
    print('Hold the Anchovies!')

requested_toppings = ['mushroom', 'onion', 'pineapple']
topping = 'mushroom'
if topping in requested_toppings:
    print(f"we found {topping} in {requested_toppings}.")
topping = 'pepperoni'
if topping in requested_toppings:
    print(f"we found {topping} in {requested_toppings}.")
else:
    print(f"didn't find {topping} toppings.")



requested_toppings = ['mushroom', 'extra cheese']
if 'mushroom' in requested_toppings:
    print('adding mushroom')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')

print('finished making pizza')

print("\npg86 checking for special items")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

print("")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry, we are out of green peppers.')
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

print("")
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('sorry, we are out of green peppers.')
        else:
            print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("are you sure you want a plain pizza?")

print("")
available_toppings = ['green peppers', 'extra cheese', 'olives', 'pineapples', 'pepperoni', 'mushrooms']
requested_toppings = ['extra cheese', 'olives', 'green peppers', 'french fries']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('sorry, we are out of green peppers.')
        elif requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"sorry, we don't have {requested_topping} pizza topping.")
    print("Finished making your pizza!")
else:
    print("are you sure you want a plain pizza?")
