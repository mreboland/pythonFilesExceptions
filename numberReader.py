import json

# Here we set the file we write to, to a variable to open
filename = "numbers.json"

# We open the file in read mode (defaults to it if nothing is specified) as python only needs to read from the file
with open(filename) as f:
    # json.load() loads the info stored in numbers.json and we assign it to a variable so we can print it.
    numbers = json.load(f)
    
print(numbers)