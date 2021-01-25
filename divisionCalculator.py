# Exception
# Python uses special objects called exceptions to manage errors that arise during a program's execution. When an error occurs, an exception object is created. If we write code to handle this exception, the program will continue running. If we don't we'll get a traceback error and the program will end.
# Exceptions are handled with a try-except block

# Handling the ZeroDivisionError exception
# We can't divide by zero
# Gives us a traceback error with ZeroDivisionError
# print(5/0)

# Using try-except blocks

# the try attempts to run the code, if the code causes an error, python will skip over the try and run the except block of code. 
try:
    print(5/0)
# Putting the error after except isn't necessary. It still captures the error.
except ZeroDivisionError:
    # In our case this print statement is run because we can't divide by zero. However, to note, we didn't get an error in the terminal like we did when we ran print(5/0). The program continued.
    print("You can't divide by zero!")
    
# Using exceptions to prevent crashes

# print("Give me two numbers, and i'll divide them.")
# print("Enter 'q' to quit.")

# Basic program to accept a user's input so we can calculate the division
# This will break when we divide by zero
# while True:
#     firstNumber = input("\nFirst number: ")
#     if firstNumber == "q":
#         break
    
#     secondNumber = input("Second number: ")
#     if secondNumber == "q":
#         break
    
    # Because input data is a str, we need to convert it to an integer in order to do math
    # answer = int(firstNumber) / int(secondNumber)
    # print(answer)
    
# It's bad for a program to crash, however it's even worse to let users see tracebacks. Nontechnical users will be confused by them, in a malicious setting, the user will learn more than you want them too. They'll see the name of the program file, they'll see a part of our code isn't working. A skilled attacker could potentially use it to attack our code.

# The else block

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    firstNumber = input("\nFirst number: ")
    if firstNumber == "q":
        break

    secondNumber = input("Second number: ")
    if secondNumber == "q":
        break

    # We ask python to try to complete the division operation in a try block. This block only contains the code that may break
    try:
        answer = int(firstNumber) / int(secondNumber)
    # The except block tells python how to respond when a ZeroDivisionError arises. If the try block doesn't succeed, we print a friendly message telling the user how to avoid this kind of error. The program continues to run, and the user never see a traceback.
    except (ZeroDivisionError):
        print("You can't divide by 0!")
    # Any code that depends on the try block succeeding is added to the else block to print the result
    else:
        print(answer)

