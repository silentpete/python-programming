first_name = 'Peter'
last_name = 'Gallerani'

# example 1, we'll cat the output together to make the greeting
greeting = 'Hello, ' + first_name + ' ' + last_name
print(greeting)

# example 2, we can use format with placeholders
greeting = 'Hello, {} {}'.format(first_name, last_name)
print(greeting)

# example 3, use the format with defined placement
greeting = 'Hello, {1} {0}'.format(first_name, last_name)
print(greeting)

# example 4, with python 3...
greeting = f'Hello, {first_name} {last_name}'
print(greeting)
