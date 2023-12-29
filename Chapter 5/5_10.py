curent_users = ["Alex", "Viktoria", "Dorotea", "Admin"]

new_users = [
    "aleX",
    "viktor",
    "summer",
    "cody",
    "zac",
]

check_users = curent_users[:]
check_users = [check_user.lower() for check_user in check_users]
# print(check_users)

for new_user in new_users:
    if new_user.lower() in check_users:
        print(f"This name {new_user} is unavailable")
    else:
        print(f"This name {new_user} is available")
