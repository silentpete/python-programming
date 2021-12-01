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
