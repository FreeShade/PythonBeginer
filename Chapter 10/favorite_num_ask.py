import json

favorite_num = input("What is your favorite number? ")
filename = "fnumber.json"
with open(filename, "w") as f:
    json.dump(favorite_num, f)
# """питає та запам'ятовує улюблене число"""


# # import json

# # username = input('What is your name ? ')

# # filename = 'username.json'
# # with open(filename, 'w') as f:
# #     json.dump(username, f)
# #     print(f"We'll remembr you when you come back, {username}!")
