done_with_toppings_keyword = 'done'
prompt = "\nWhat pizza topping would you like on your pizza (one at a time)?: "
prompt += f"\n(enter '{done_with_toppings_keyword}' after all your toppings have been entered) "

taking_toppings = True
while taking_toppings:
    topping = input(prompt)

    if topping == done_with_toppings_keyword:
        break
    else:
        print(f"I'll add {topping} topping to your pizza")

print("\nThank you for your toppings")
