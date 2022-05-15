players = ['charles', 'martina', 'michael', 'florance', 'eli']
# list elements start at index 0
# print from 0 index to index 3
print(players[0:3])

# print index 1 - 4
print(players[1:4])

# print starting at the beginning up to the 4th index
print(players[:4])

# print from index 3 to the end
print(players[3:])

# print last three values in list
print(players[-3:])

# print from index one till the end and only every other value
print(players[1::2])

# print from the beginning of the list to the end and only every other value
print(players[::2])


print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
