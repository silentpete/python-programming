my_list = [1,2,3,4,5,6]

print('list before: ' + str(my_list))

for i in my_list:
  if i == 2:
    my_list.remove(2)

print('list after: ' + str(my_list))

my_str_list = ['peter', 'david', 'john', 'ricca']

print('str list before: ' + str(my_str_list))

for i in my_str_list:
  if i == 'peter':
    my_str_list.remove(i)

print('str list after: ' + str(my_str_list))
