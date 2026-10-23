current_users = ["John", "Mary", "David", "Sarah", "Robert"]
new_users = ["john", "Alice", "mary", "Tom", "Emma"]

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"{new_user} has already been used. You will need to enter a new username.")
    else:
        print(f"{new_user} is available.")