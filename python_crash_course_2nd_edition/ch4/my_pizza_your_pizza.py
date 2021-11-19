my_pizzas = ['pepperoni', 'chicken parm with tomato', 'ham and pineapple']
friend_pizzas = my_pizzas[:]

my_pizzas.append('rasberry, ricotta and pepperoni')
friend_pizzas.append('veggie')

print("My favorite pizzas are:")
for p in my_pizzas:
    print(p)

print("My friends favorite pizzas are:")
for p in friend_pizzas:
    print(p)
