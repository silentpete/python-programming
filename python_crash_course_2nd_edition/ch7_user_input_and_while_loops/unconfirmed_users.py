# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unverified_users = ['alice', 'Azure', 'brian', 'candace']
verified_users = []

# Verify each user until there are no more unverfied users.
# Move each verified user into the list of verfied users.
while unverified_users:
    current_user = unverified_users.pop()

    print(f"Verifying user: {current_user.title()}")
    verified_users.append(current_user.lower())

# Display all verified users.
print("\nThe following users have been verified:")
verified_users.sort()
for vu in verified_users:
    print(vu.title())
