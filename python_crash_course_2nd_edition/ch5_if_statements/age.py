age = 21

print(age >  18)
print(age >= 18)
print(age <  18)
print(age <= 18)

age_0 = 22
age_1 = 18
drinking_age = 21

if age_0 >= drinking_age and age_1 >= drinking_age:
    print('true')
else:
    print('false')

if age_0 >= drinking_age and age_1 + 3 >= drinking_age:
    print('true')
else:
    print('false')

if age_0 >= drinking_age or age_1 >= drinking_age:
    print('true')
else:
    print('false')
