# Saving and reading user-generated data
# Saving data with json is useful when we're working with user-generated
# data, because if you don’t store your user’s information somehow, you’ll
# lose it when the program stops running.

# An example where we prompt a user for their name and store it on first run. Then remember the name when they run the program again
import json
# Prompt the user for their name
# username = input("What is your name? ")
# # File to save user's name to
# filename = "username.json"
# with open(filename, "w") as f:
#     # Store user's name in username.json
#     json.dump(username, f)
#     # Informing user we'll remember them
#     print(f"We'll remember you when you come back, {username}!")
    

# adding greetUser.py functionality back into this program:

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = "username.json"

# There's no new code in this block from the above code and the code in greetUser.py
try:
    # first we try to open the file username.json to see if the user already exists. If they don't it'll kick up an error which will move us into the except code block where we create a new user.
    with open(filename) as f:
        # We load the username if it exists and save it to the var username. It would get printed in the else block if it exists
        username = json.load(f)
# If the user is new, this code block will run
except FileNotFoundError:
    # Get user's name and save it to a variable
    username = input("what is your name? ")
    # Open a new file to write to
    with open(filename, "w") as f:
        # store user's name in username.json
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# Refactoring
# Often we'll come to a point where our code will work, but you'll recognize that it could be improved by breaking it up into a series of functions that have specific jobs.
# Refactoring makes our code cleaner, easier to understand, and easier to extend

# Let's refactor our code from earlier:

# This function retrieves a stored username and return the username if it finds one. If the file username.json doesn't exist, the function returns "None". A function should either return the value you're expecting, or it should return "None".
def getStoredUsername():
    """Get stored username if available"""
    filename = "username.json"
    
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        # Return username value to call line in greetUser()
        return username
    
def getNewUserName():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = "username.json"
    
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def greetUser():
    # Using a function requires a docstring
    """Greet the user by name"""
    # call the function to see if we have a username, if we don't, a "None" value is returned sending use into the "else" block to register a new user
    username = getStoredUsername()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = getNewUserName()
        print(f"We'll remember you when you come back, {username}!")

greetUser()

# Each function in this final version of remember_me.py has a single, clear
# purpose. We call greetUser(), and that function prints an appropriate message:
# it either welcomes back an existing user or greets a new user. It does
# this by calling getStoredUsername(), which is responsible only for retrieving
# a stored username if one exists. Finally, greetUser() calls getNewUsername()
# if necessary, which is responsible only for getting a new username and storing
# it. This compartmentalization of work is an essential part of writing
# clear code that will be easy to maintain and extend.


# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

# filename = "favNum.json"

# num = input("What is your favourite number? ")

# with open(filename, "w") as f:
#     json.dump(num, f)


# 10-12. Favorite Number Remembered: Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

filename = "favNum.json"

try:
    with open(filename) as f:
        favNum = json.load(f)
except FileNotFoundError:
    num = input("What is your favourite number? ")
    with open(filename, "w") as f:
        json.dump(num, f)
else:
    print(f"I know your favourite number! It's {favNum}!")


# 10-13. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who
# last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.

def getStoredUsername():
    """Get stored username if available"""
    filename = "username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    

def getNewUserName():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = "username.json"

    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greetUser():
    """Greet the user by name"""
    username = getStoredUsername()
    # If we have a username
    if username:
        # Prompt user to check if it is them
        userCheck = input(f"Is {username} you? (y/n) ")
        # If it is, welcome them back
        if userCheck.lower() == "y":
            print(f"Welcome back, {username}!")
        # If not, call getNewUserName to save them
        else:
            getNewUserName()
    else:
        username = getNewUserName()
        print(f"We'll remember you when you come back, {username}!")


greetUser()
