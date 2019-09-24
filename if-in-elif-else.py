state = input('what state do you live in? ')

if state.lower() in('michigan', 'arizona', 'colorado'):
  print('peter has lived here')
elif state.lower() in ('idaho', 'montana', 'ohio', 'kentucky'):
  print('peter is thinking about moving to that state')
elif state.lower() == 'florida':
  print('eww')
else:
  print('oh, that state')
