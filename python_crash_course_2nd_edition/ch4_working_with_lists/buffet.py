foods = ('chicken', 'pizza', 'pasta', 'cookies', 'salad')

print("we serve the following foods")
for food in foods:
    print(food)

# The following line will error
#foods[0] = 'apples'
# Error Output
# Traceback (most recent call last):
#   File "c:\dev\code\github.com\silentpete\python-programming\python_crash_course_2nd_edition\ch4\buffet.py", line 7, in <module>
#     foods[0] = 'apples'
# TypeError: 'tuple' object does not support item assignment

print("\nWe are changing our menu")
foods = ('turkey', 'pizza', 'pasta', 'soup', 'salad')
print("we serve the following foods")
for food in foods:
    print(food)
