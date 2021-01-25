# Writing to a file
# One of the simplest ways to save data is to write to a file. When we write text to a file, the output will still be available after we close the terminal containing our programs output

# Writing to an empty file
# To write to a file, we need to call open() with a second argument telling python that you want to write to the file.

filename = "programming.txt"

# Here we 'open' a file like normal. The 'w' tells python that we want to open the file in 'write mode'. We can open in read mode 'r', write mode 'w', append mode 'a', and read and write 'r+'.
# If we leave out the argument, python defaults to read only.
# If the file doesn't exist, open() will automatically create the file. However, we need to be cautious as if we open a file in write mode, 'w', and the file exists, python will erase the contents of the file before returning the file object
with open(filename, "w") as file_object:
    # Here we are writting a string to the file
    file_object.write("I love programming.")
    
# Python cal only write string to a text file. If we want to store numerical data in a text file, we'll have to convert the data to string format first using the str() function

# Writing multiple lines
# The write() function doesn't add any newlines to the text we write. So if we want to write more than one line without including newline characters, our file won't look like the way we want it to

filename = "programming.txt"
with open(filename, "w") as file_object:
    # When we open programming.txt after this code block runs, we'll see that the lines are squished together
    # I love programming.I love creating new games.
    # To solve the issues we need to include newlines \n
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
# Append to a file
# If we want to add content to a file instead of writing over existing content, we open the file in append mode.
# In append mode python doesn't erase any data, it adds it to the end of the file.
# If the file doesn't exist, it'll be created

filename = "programming.txt"

# We use the 'a' argument to open the file for appending rather than writing over the existing file
with open(filename, "a") as file_object:
    # Here we are writing two news lines which get added at the end of our earlier lines
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.

filename = "guest.txt"

# with open(filename, "w") as file_object:
#     username = input("What is your name? ")
#     file_object.write(username)

# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

filename = "guestBook.txt"

with open(filename, "a") as file_object:
    while True:
        print("What is your name?")
        username = input("Enter 'q' at anytime to quit ")
        
        if username == "q":
            break
        
        print(f"\nHello {username.title()}!")
        file_object.write(f"{username}\n")

# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

filename = "programmingPoll.txt"

with open(filename, "a") as file_object:
    while True:
        print("Why do you like programming?")
        poll = input("Enter 'q' at anytime to quit ")

        if poll == "q":
            break
        
        file_object.write(f"{poll}\n")

