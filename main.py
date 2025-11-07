# Terry Terwilliger  ---  11/7/2025  ---  HW 3B
# Description: This program will generate a unique user ID based on their first & last name.
# The users ID will have the first letter of their first name and then followed by the first five letters of their last name & also a random two digit number ranging from 10-99.


import random

# makeID takes two names their first and last creates a userID
# and returns something that looks like tterwi25
def makeID(firstName, lastName):
    # Makes sure all characters are uppercase
    firstName = firstName.upper()
    lastName = lastName.upper()

    # Extract the first inital of their first name
    id_part1 = firstName[0]

    # Extract the first five ...
    id_part2 = lastName[:5]

    # Get a random number between 10 and 99
    myNumber = random.randrange(10 ,99)

    # Put it all together (concatenate)
    userID = id_part1 + id_part2 + str(myNumber)
    return userID


# main will ask the user to enter their first and last name, then it calls and prints a generated userID also warning the user not to share their ID with anyone else.
def main():
    # Ask for their first name
    firstName = input("To continue please enter your first name: ")

    # Ask for their last name
    lastName = input("Now please enter your last name to complete the process: ")

    # Call makeID
    userID = makeID(firstName, lastName)

    # Print out the userID
    print("Your unique userID for the program is:", userID,", I recommend not sharing it with anyone" ) 


# Function definitions above
############################
# Test code below
main()
