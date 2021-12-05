print("pg 105 6-5")
rivers = {"nile": "egyt", "mississippi": "united states", "danu": "germany"}
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("the rivers")
for r in rivers.keys():
    print(r)
print("the countries")
for c in rivers.values():
    print(c)
