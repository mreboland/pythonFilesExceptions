# Working with multiple files

# The below code block is mostly the same from alice.py other than we moved it into a function which takes the parameter filename which gets it's data from the argument we call the function with
def countWords(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()

    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the approx number of words in the file
        words = contents.split()
        numWords = len(words)
        print(f"The file {filename} has about {numWords} words.")

filename = "alice.txt"
countWords(filename)

# By putting our word count program in a function we can now call it as many times as we want for as many books as we want
# We can do so by looping over a list of books
filenames = ['alice.txt', 'siddhartha.txt',
             'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    countWords(filename)
    
# Using the try-except block in this example provides two significant
# advantages. We prevent our users from seeing a traceback, and we let the
# program continue analyzing the texts it’s able to find. If we don’t catch
# the FileNotFoundError that siddhartha.txt raised, the user would see a full
# traceback, and the program would stop running after trying to analyze
# Siddhartha. It would never analyze Moby Dick or Little Women.


# Failing silently
# In the previous example, we informed our users that one of the files was unavailable. However we don't need to report every exception we catch. To make a program fail silently, we write a try block as usual,, but we explicitly tell python to do nothing in the except block.

# except FileNotFoundError:
    # print(f"Sorry, the file {filename} does not exist.")
    
# to:

# except FileNotFoundError:
#     pass
    
# The pass statement tells python to ignore the error and not output anything. So in the previous example of siddhartha.txt being missing wouldn't show if we used pass instead. See above to test.
# Pass also acts as a placeholder. It is a reminder that we've chose to do nothing. Maybe in the future we'll want to write the missing novel to missingFiles.txt instead. Users won't be able to see any missing files and we can read it to deal with it.

# Deciding which errors to report
# If users know which texts are supposed to be analyzed, they might
# appreciate a message informing them why some texts were not analyzed. If
# users expect to see some results but don’t know which books are supposed
# to be analyzed, they might not need to know that some texts were unavailable.
# Giving users information they aren’t looking for can decrease the
# usability of your program

# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a ValueError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

# firstNumber = input("Enter first number to be added: ")
# secondNumber = input("Enter second number: ")

# try:
#     addition = int(firstNumber) + int(secondNumber)
# except ValueError:
#     print("You cannot add up letters!")
# else:
#     print(addition)

# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

# while True:
#     firstNumber = input("Enter first number to be added: ")
#     if firstNumber == "q":
#         break
    
#     secondNumber = input("Enter second number ('q' to quit): ")
#     if secondNumber == "q":
#         break
    
#     try:
#         addition = int(firstNumber) + int(secondNumber)
#     except ValueError:
#         print("You cannot add up letters!")
#     else:
#         print(addition)


# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a different
# location on your system, and make sure the code in the except block
# executes properly.

def animalNames(filename):
    
    try:
        with open(filename, "r") as f:
            contents = f.read()
    except:
        print(f"The {filename} is missing.")
    else:
        print(contents)
        
files = ["dogs.txt", "cats.txt"]
for file in files:
    animalNames(file)


# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

def animalNames(filename):

    try:
        with open(filename, "r") as f:
            contents = f.read()
    except:
        pass
    else:
        print(contents)

files = ["dogs.txt", "cats.txt"]
for file in files:
    animalNames(file)

# 10-10. Common Words: Visit Project Gutenberg(https: // gutenberg.org /)
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >> > line = "Row, row, row your boat"
# >> > line.count('row')
# 2
# >> > line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text. This will be
# an approximation because it will also count words such as 'then' and 'there'.
# Try counting 'the ', with a space in the string, and see how much lower your
# count is .

def theCount(filename):
    """Counting the amount of times 'the' appears in a novel"""
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    
    # 'the' will capture all the along with words with 'the' in it like them, then, etc
    print(f"\n{text.count('the')}")
    # Adding the space after 'the' guarantees the word the 'the' itself
    print(text.count("the "))
    # using lower will allow us to count the "The" as well
    print(text.lower().count("the"))

filename = "alice.txt"
theCount(filename)
