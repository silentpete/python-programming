print("pg 106 list of dictionaries")
alien_0 = {"color": "green", "points": "5"}
alien_1 = {"color": "yellow", "points": "10"}
alien_2 = {"color": "red", "points": "15"}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("generate aliens")
aliens = []
# make 30 green aliens
for alien_number in range(30):
    new_alien = {"id": alien_number, "color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fase'
        alien['points'] = 15
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
