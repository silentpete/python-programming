favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

for name, language in favorite_languages.items():
    if language.lower() == "c":
        print(f"{name.title()}'s favorite language is {language.upper()}.")
    else:
        print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

# by default, the above would work without defining keys() since it is the default action
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}.")

if 'eric' not in favorite_languages.keys():
    print("Erin, please take our poll.")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned")
for language in favorite_languages.values():
    print(language.title())
print("use set() to remove duplicates")
for language in set(favorite_languages.values()):
    print(language.title())
print("use sorted(set()) to get a sorted list and remove duplicates")
for language in sorted(set(favorite_languages.values())):
    print(language.title())

print("\npg 109")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
