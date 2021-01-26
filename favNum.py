import json

filename = "favNum.json"

with open(filename) as f:
    favNum = json.load(f)
    print(f"I know your favourite number! It's {favNum}!")
