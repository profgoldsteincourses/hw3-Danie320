# Add appropriate comments...such as your name, the date...

import random

# makeID takes two ...
# and returns...
def makeID(first, last):
    # Extract the first inital of their first name

    first_name = first[0]

    # Extract the first five ...

    last_name = last[0:5]

    # Get a random number between 10 and 99
    myNumber = random.randrange(10, 100)

    # Put it all together (concatenate)

    ID = first_name + last_name + str(myNumber)

    return ID


# main prompts the user ....
def main():
    # Ask for their first name

    firstName = input("What is your first name? ")

    # Ask for their last name

    lastName = input("What is your last name?: ")

    # Call makeID
    newID = makeID(firstName, lastName)

    # Print out the newID
    print(newID)


# Function definitions above
############################
# Test code below
main()
