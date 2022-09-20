def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimmy", "hendrix")
print(musician)

# add optional middle name
def get_formatted_name_b(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_b("jimmy", "hendrix")
print(musician)
musician = get_formatted_name_b(first_name="john", middle_name="lee", last_name="hooker")
print(musician)
