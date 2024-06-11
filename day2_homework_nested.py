# 1. Nested Decisions: The Adventure Game 🏰
# Objective 1: To practice the use of nested if statements in creating a simple text-based adventure game.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.
# Buggy Code:

# place = input("Choose a place: forest or cave? ")
# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

place = input("Choose a place: forest or cave? ")

if place == "forest": #Changed to ==
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": #Changed to == 
        print("You found a bird's nest!")
    else: # Dont need anything after an Else. 
        print("You found a boat!")
elif place == "cave": #Changed to ==
    print("You find a hidden treasure!")

# Task 2: Setting the Scene

# Based on the corrected code from Task 1, expand the game. 
# If the user chooses "cave", instead of printing "You find a hidden treasure!" ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": 
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
#Expanded on the cave scenario 
elif place == "cave": 
    action = input("light a torch or proceed in the dark") #added an action to take.
    if action == "light a torch": # if you light a torch then you can see treasure
        print("You find a hidden treasure!")
    else: 
        print("You cant see anything guess its time to leave.") #otherwise you dont see the treassure and leave. 


# Task 3: Default Path
#If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree": 
        print("You found a bird's nest!")
    elif action == "cross a river": #Changed the else to actually take the second input and give an output for it. 
        print("You found a boat!")
    else:
        pass #added a pass to the else.
elif place == "cave": 
    action = input("light a torch or proceed in the dark")
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark": #Changed the else to actually take the second input and give an output for it. 
        print("You cant see anything guess its time to leave.")
    else:
        pass # added a pass to the else.




#2. Quick Decisions: The Event Planner 🎉
#Objective: To practice the use of shorthand if statements in determining event-related decisions.

#Task 1: Code Correction
#You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
#Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)

attendees = int(input("Enter number of attendees: ")) # Changed input to an integer. 
venue = "large hall" if attendees > 100 else "conference room" # Changed elif to else
print(venue)

food_type = input("Do you want want vegetarian food - yes/no:") # Asking if they want a vegetarian meal.
meal_type = "Veggie Delight Caterer" if food_type == "yes" else "Gourmet Meals Caterers" # If the same yes it spits out "Veggie Delight Caterer" if they say aything else it spits out "Gourmet Meals Caterers"
print(meal_type)

