# reference https://docs.python.org/3.6/reference/compound_stmts.html#try

x = 4
y = 0

try:
  print(x/y)
except ZeroDivisionError as e:
  print('exception occured: not allowed to divide by zero')
else:
  print('else: The optional else clause is executed if the control flow leaves the try suite, no exception was raised, and no return, continue, or break statement was executed. Exceptions in the else clause are not handled by the preceding except clauses.')
finally:
  print('finally: run cleanup handler')
