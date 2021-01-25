# piDigits contains pi to 30 decimals, 10 places per line

# Reading an entire file
# In order to work with a file, we must 'open' the file in order to access it. The 'open' function needs one argument, the name of the file. Python looks for the file in the directory the current program is being executed in.
# The open function returns an object representing the file, and python assigns the object to 'file_object'.
# The keyword 'with' closes the file once access to it is on longer needed. We call open in this program but never close(). We could use it however improper use could result in trying to work with a closed file resulting in data lost or corruption. To avoid any potential mishaps, we let python do the work for us using the 'with' block.
with open("piDigits.txt") as file_object:
    # Once we have a file object representing piDigits.txt, we use read() method to read the entire contents of the file and store it as one long string in our variable contents.
    contents = file_object.read()
# read() returns an empty string when it reaches the end of the file. It shows itself as a blank line. If we want to remove it, we can use rstrip() in the print.
print(contents.rstrip())

# File paths
# If our text file (due to us using organization to keep files in separate folders), is not in the main folder, we can use relative file pathing to get access to it.
# For example our file is in a folder called textFiles
# with open("textFiles/filename.txt") as file_object:

# We could also use absolute file path which is literally the path breakdown from home
# Example:
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# Reading line by line
# When we're reading a file, we'll often want to examine each line of the file. To do so, we need to loop over the file object to examine each line.

# Here we assign the file we're reading to a variable. This is common convention when working with files. This allows us to change the filename associated with the variable saving us the need to modify our code blocks.
print("\n")
filename = "piDigits.txt"

# We 'open' filename which is linked to our file
with open(filename) as file_object:
    # Loop over each line of our file which we print out
    for line in file_object:
        # On our print, there are blank lines between each line. Like mentioned earlier, a newline character is printed at the end. Because each line is it's own end, a newline gets printed. To remove it we use rstrip()
        print(line.rstrip())


# Making a list of lines from a file
# When we use with, the file we are working with is only available within the with block that contains it. If we want to use the file's contents outside the with block, we can store the file's lines in a list inside the block.

print("\n")
filename = "piDigits.txt"

with open(filename) as file_object:
    # readlines() takes each line from the file and stores it in a list. This list is then assigned to 'lines' which we can work with after the with block ends
    lines = file_object.readlines()

# Here we use a simple for loop to print each line
for line in lines:
    print(line.rstrip())
