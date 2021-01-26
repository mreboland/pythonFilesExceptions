# Using json.dump() and json.load()
# We'll write a short program that stores a set of numbers and another program
# that reads these numbers back into memory. The first program will
# use json.dump() to store the set of numbers, and the second program will use
# json.load().

# json.dump() takes two arguments. A piece of data to store and a file object it can use to store the data
import json

numbers = [2, 3, 5, 7, 11, 13]

# We choose a filename in which to store the list of numbers. It's customary to use the file extension .json to indicated the data is stored in that format
filename = "numbers.json"
# We open the file in write mode so we can write data to it
with open(filename, "w") as f:
    # We use json.dump() to store the list "numbers" in the file numbers.json
    json.dump(numbers, f)
    
    