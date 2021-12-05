alien = {'color': 'black', 'speed': 'slow'}
#print(alien['points'])
# Output:
# Traceback (most recent call last):
#   File "c:\dev\code\github.com\silentpete\python-programming\python_crash_course_2nd_edition\ch6\alien_no_points.py", line 2, in <module>
#     print(alien['points'])
# KeyError: 'points'

point_value = alien.get('points', 'no point assigned')
print(point_value)
