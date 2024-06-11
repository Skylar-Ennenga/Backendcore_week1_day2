
# Lesson 2: The Magic of Conditional Statements: Assignments: Dive Deeper

# Objective 1 - Buggy Code:
# Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# number = input("Enter a number: ")
# if number > 0:
#     print("The number is positive.")
# elif number = 0:
#     print("The number is zero.")
# else number < 0:
#     print("The number is negative.")

number = int(input("Enter a number: ")) # Need to make the input an integer.

if number > 0:
    print("The number is positive.")
elif number == 0: # needs to be == so it can equate and not set it to 0. 
    print("The number is zero.")
else: # doesnt need anything after the else since else just take anything thats left.
    print("The number is negative.")




# Objective 2: Harness the power of conditional statements to compare and determine values.

# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. The program should then identify and print out the largest number among the three.
# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The largest number is 4.".
# User provides 3 numbers that will then be evaluated. 

first_number = int(input("Please enter a number: "))
second_number = int(input("Please enter a second number: "))
third_number = int(input("Please enter a third number: "))

if first_number > second_number and first_number > third_number: # If the first number is greater than the other 2 it is the largest. 
    largest_number = first_number
    print(f"The largest number is {first_number}") # Im glad we got to learn the format in class today this looks much better. 
elif second_number > first_number and second_number > third_number: # If the second number is greater than the other 2 it is the largest. 
    largest_number = second_number
    print(f"The largest number is {second_number}") 
else: # If neither the above are true the it defaults to third number being the largest.
    print(f"The largest number is {third_number}")