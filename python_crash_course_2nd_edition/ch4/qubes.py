qubes = []
for value in range(1,11):
    qube = value**3
    qubes.append(qube)

print(qubes)

qubes = [value**3 for value in range(1,11)]
print(qubes)
