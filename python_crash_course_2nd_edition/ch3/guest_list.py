guest_list = ['mark', 'nicole', 'teddy']

print("=== 3.4 - invite each guest to dinner ===")
print(f"Hello {guest_list[0].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[1].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[2].title()}, would you like to come to dinner?")

print("\n=== 3.5 - someone else to invite ===")
cannot_make_it = 'teddy'
print(f"{cannot_make_it.title()} can't make it.")
new_guest = 'phil'
guest_list.remove(cannot_make_it)
guest_list.append(new_guest)
print(f"Hello {guest_list[0].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[1].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[2].title()}, would you like to come to dinner?")

print("\n=== 3.6 - bigger table ===")
print("found a bigger table")
guest_list.insert(0, 'lori')
guest_list.insert(2, 'heather')
guest_list.append('perry')
print(f"Hello {guest_list[0].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[1].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[2].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[3].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[4].title()}, would you like to come to dinner?")
print(f"Hello {guest_list[5].title()}, would you like to come to dinner?")

print("\n=== 3.7 - shucks, won't arrive ontime ===")
print('can only invite two people')
say_sorry = guest_list.pop()
print(f"Sorry {say_sorry.title()}, only two people will fit at the table.")
say_sorry = guest_list.pop()
print(f"Sorry {say_sorry.title()}, only two people will fit at the table.")
say_sorry = guest_list.pop()
print(f"Sorry {say_sorry.title()}, only two people will fit at the table.")
say_sorry = guest_list.pop()
print(f"Sorry {say_sorry.title()}, only two people will fit at the table.")
print(f"{guest_list[0].title()}, you are still invited to dinner.")
print(f"{guest_list[1].title()}, you are still invited to dinner.")
del guest_list[0]
del guest_list[0]
print(guest_list)