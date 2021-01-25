# Handling the FileNotFoundError exception
# One common issue when working with files is handling missing files. The
# file you’re looking for might be in a different location, the filename may
# be misspelled, or the file may not exist at all. You can handle all of these
# situations in a straightforward way with a try-except block.

# With no alice.txt in our root directory, we'll get an error with the below code
filename = "alice.txt"

# The variable 'f' here is used to represent file_object. It is a common convention.
# The 'encoding' argument is needed when your system's default encoding doesn't match the encoding of the file that's being read.
# We get a FileNotFoundError exception as a result of open running
# with open(filename, encoding="utf-8") as f:
#     contents = f.read()

# To correct it:

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# Analyzing text

# To count the number of words in the text we'll use split()
title = "Alice in Wonderland"
# split() method separates a string into parts wherever it finds a space and stores all the part of the string in a list
print(title.split())

# To count the number of words in alice.txt (we since added after earlier example)

filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approx number of words in the file
    # Here we take the string 'contents' which contains the entire text of Alice in Wonderland as one long string, and we use split() method to produce a list of all the words in the book
    words = contents.split()
    # Because we now have a 'list' of words, we can use len to determine the length of the list to get an approx representation (due to publisher info, etc) of the words in the novel. We save it to a variable to print out.
    numWords = len(words)
    print(f"The file {filename} has about {numWords} words.")
    # The code in this else block is here because it'll only work if the code in the try block was executed successfully