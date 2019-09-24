country = input('what country are you from? ')
state_or_province = input('what state or province do you live in? ')

if country.lower() == 'canada':
  if state_or_province.lower() == 'alberta':
    print('woe, you are up there')
  else:
    print('that is not to cold')
elif country.lower() in ('usa', 'u.s', 'u.s.a.'):
  if country.lower() == 'colorado':
    print('hell yea! that is right')
  else:
    print('please leave')
