import json

filename = "username.json"

with open(filename) as f:
    # We use json.load to read the info in username.json and assign it to a variable to use.
    username = json.load(f)
    print(f"Welcome back, {username}!")
    
# We will combine the above program in rememberMe to better reflect one program doing it all.