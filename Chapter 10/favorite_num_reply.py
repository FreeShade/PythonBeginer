import json

filename = "fnumber.json"
with open(filename) as f:
    favorite_num = json.load(f)

print(f"I know your favorite number is {favorite_num}")
