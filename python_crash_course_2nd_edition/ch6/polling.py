print("pg 105 6-6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = {"peter", "nicole", "jen", "mark", "edward"}

for name in poll_takers:
    if name in favorite_languages.keys():
        print(f"Thank you for responding, {name.title()}.")
    else:
        print(f"{name.title()}, can you please take our poll?")
