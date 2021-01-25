# Working with a file's contents

# Let's attempt to build a single string containing all the digits in the file with no whitespace in it
filename = "piDigits.txt"

# Saving file contents into list using readlines()
with open(filename) as file_object:
    lines = file_object.readlines()
    
# We create an empty variable to hold the digits of pi
piString = ""
# We loop over the lines in our file saved to 'lines'
for line in lines:
    # For each line read, we strip the whitespace and add it to our variable piString
    # Adding strings together tacks them onto to each other
    piString += line.rstrip()

# Here we print our string and also show how long it is
print(piString)
print(len(piString))

# vsCode's terminal doesn't show the whitespace however the output should look like
# 3.1415926535 8979323846 2643383279
# using rstrip(). This is because there is also white space on the left side of the digits in each line. To get rid of that we use strip()
# for line in lines:
        # piString += line.strip()
# The above may not be accurate as i've tested with different text editors and pythons shell, and rstrip() shows the data correctly*

# As a note, python reads a file as a string only. So if you're working with numbers we'll have to convert those numbers to and integer using the int() function, or a float() (decimals)

# Large files: One million digits
# Our initial pi file is small and only contains three lines. However our code in the above example will work just fine with much large files.
# The only change we'd need to make to our original program is the filename and maybe limit the amount of lines printed for brevity

filename = "piMillionDigits.txt"

# Saving file contents into list using readlines()
with open(filename) as file_object:
    lines = file_object.readlines()

# We create an empty variable to hold the digits of pi
piString = ""
# We loop over the lines in our file saved to 'lines'
for line in lines:
    # For each line read, we strip the whitespace and add it to our variable piString
    # Adding strings together tacks them onto to each other
    piString += line.rstrip()

# Here we print our string and also show how long it is
# We use a slice to only print the first 50 decimal places (it's 52 because we need to account for 3. in pi which are 2 "places")
print(piString[:52])
print(len(piString))

# Python has no inherent limit to how much data you can work with; you can work with as much data as your system's memory can handle.

# Is our birthday contained in pi?
# Lets do a little project to see if someone's birthday appears anywhere in the first million digits of pi.
# We can do this by expressing each bday as a string of digits and seeing if that string appears anywhere in pi

filename = "piMillionDigits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    piString += line.strip()
    
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in piString:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# 10-1. Learning Python: Open a blank file in your text editor and write a few
# lines summarizing what you’ve learned about Python so far. Start each line
# with the phrase In Python you can. . . . Save the file as learning_python.txt in
# the same directory as your exercises from this chapter. Write a program that
# reads the file and prints what you wrote three times. Print the contents once by
# reading in the entire file, once by looping over the file object, and once by storing
# the lines in a list and then working with them outside the with block.

filename = "learningPython.txt"

print("\nRead file:")
with open(filename) as file_object:
    contents = file_object.read()
    
print(contents)

print("\nLooping within 'with':")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\nList")
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.strip())


# 10-2. Learning C: You can use the replace() method to replace any word in a
# string with a different word. Here’s a quick example showing how to replace
# 'dog' with 'cat' in a sentence:
# >> > message = "I really like dogs."
# >> > message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C. Print
# each modified line to the screen.

filename = "learningPython.txt"
print("\n")

# Easiest way to modify value by printing the change from the file as we loop over the lines
with open(filename) as file_object:
    for lines in file_object:
        print(lines.replace("Python", "C"))
        
# Saving file to list
with open(filename) as file_object:
    lines = file_object.readlines()

# Similar to the first way, we just print the change as we loop over the list.
for line in lines:
    print(line.replace("Python", "C"))
    
# If we want to update the list itself, we need to get the position of the list and save the update to that position through a loop
for pos in range(len(lines)):
    lines[pos] = lines[pos].replace("Python", "C")
    
# Print line by line to show that the list was updated
for line in lines:
    print(line)
