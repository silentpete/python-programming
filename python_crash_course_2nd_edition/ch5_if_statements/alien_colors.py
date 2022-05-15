alien_color = 'green'

if alien_color == 'green':
    print('you just earned 5 points')


alien_color = 'yellow'
if alien_color == 'green':
    print('you just earned 5 points')
elif alien_color == 'yellow' or alien_color == 'red':
    print('you just earned 10 points')


alien_color = 'yellow'
if alien_color == 'green':
    print('you just earned 5 points')
elif alien_color == 'yellow':
    print('you just earned 10 points')
else:
    print('you just earned 15 points')
