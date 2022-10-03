def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("peter", "gallerani", location='colorado springs', field='IT')
print(user_profile)
user_profile = build_profile("nicole", "gallerani", location='colorado springs', field='Law')
print(user_profile)
user_profile = build_profile("marley", "smith", location='colorado springs', field='fluffy dog')
print(user_profile)
