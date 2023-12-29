users = ["alex", "viktoria", "zac", "dorotea", "admin"]

for user in users:
    if user in users:
        print(f"Hello {user.title()}, thank you for loggin in again.")
if "admin" in users:
    print("\nHello Admin, would you like to see a status report?")
