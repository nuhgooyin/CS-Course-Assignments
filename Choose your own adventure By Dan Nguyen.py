
##
# Choose Your Own Adventure Assignment
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/12/03
##

# Starting up message
print ("To get started with your own adventure, please provide the following.")
print ()

# Username input variable
userName = input("Your Username: ")

# First block to start telling the story
print("\n"+ userName, "is walking down the street. The road ahead is blocked.")

# Would you like to continue walking?
print("\nWould you like to continue walking?")
decisionOne = input("\nyes or no?\n")

# User continues walking?
if (decisionOne.lower() == "yes"):
    # Do you want to turn left?
    print()
    print("Do you want to turn left?")
    decisionTwo = input("\nyes or no?\n")

    # User turns left?
    if (decisionTwo.lower() == "yes"):
        # Another text block to continue story
        print()
        print(userName,"walks down crowded street.")

        # Do you want to stop by the cafe?
        print()
        print("Do you want to stop by the cafe?")
        decisionThree = input("\nyes or no?\n")

        # User stops by the cafe?
        if (decisionThree.lower() == "no"):
            # Continue story
            print()
            print(userName, "walks out to the busy street, and survives.")
            print()
            print("Congratulations! You won!")
        else:
            # If the user stops walking
            print()
            print(userName, "stopped and paused")
            print()
            print(userName, "is shot in drive by shooting.")
            print()
            print("Game Over! You lost!")

    # User does not turn left
    else:
        # Continue story
        print()
        print(userName, "walks into side alleyway, and sees a group of sketchy people.")

        # Do you run?
        print()
        print("Do you run?")
        decisionFour = input("\nyes or no?\n")

        # User runs?
        if (decisionFour.lower() == "yes"):
            print()
            print(userName, "walks out to the busy street, and survives.")
            print()
            print("Congratulations! You won!")

        else:
            print()
            print(userName, "gets threatened and killed by aggressive gang.")
            print()
            print("Game Over! You lost!")

else:
    # If the user stops walking
    print()
    print(userName, "stopped and paused")
    print()
    print(userName, "is shot in drive by shooting.")
    print()
    print("Game Over! You lost!")

# Ending message
print ()
print ("Thank you for completing your own adventure!")
