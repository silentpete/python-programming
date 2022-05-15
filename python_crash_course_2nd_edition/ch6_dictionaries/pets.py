print("pg 112, 6-8")

pets = {
    "hamberger": {
        "type": "dog",
        "owner": "terance",
    },
    "tango": {
        "type": "bird",
        "owner": "mike"
    },
}

for pet, pet_info in pets.items():
    print(f"{pet.title()}, is a {pet_info['type']}, and its owner is {pet_info['owner'].title()}.")
