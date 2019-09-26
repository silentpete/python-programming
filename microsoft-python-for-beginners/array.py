# Arrays must be of the same type
from array import array

scores = array('d')
scores.append(42)
print(scores)

scores.append(88)
print(scores)

print(scores[0])
