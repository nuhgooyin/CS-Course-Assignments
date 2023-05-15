
##
# Golf Scores Assignment - Initial Release Version 0.1
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/12/11
##

# Initial startup message
print("\nWelcome to golf score calculator! Please input the following information.\n")

# Input validation for number of holes
is_numberOfHoles_valid = False

while not is_numberOfHoles_valid:
    try:
        # Getting user input for number of holes
        numberOfHoles = int(input("Number of holes to score: "))

        # Is number of holes a negative integer or zero?
        if numberOfHoles <= 0:

            # True display error message
            print("\nThe number of holes must be an positive integer, please try again.\n")

        # False break loop
        else:
            is_numberOfHoles_valid = True

    # False display error message
    except:
        print("\nThe number of holes must be an positive integer, please try again.\n")

# Creates array of size numberOfHoles
scores = [0] * numberOfHoles

# Loops through array of holes
for i in range(numberOfHoles):

    # Input validation for score
    is_score_valid = False
    while not is_score_valid:

        # Gets input of score on hole
        score = input(f"\nScore on hole {i + 1}: ") # String interpolation

        # Checks if score is valid
        if not score in ["bogey", "par", "birdie", "eagle"]:
            print("\nInvalid Score, Try again.")

        # Breaks loop if score is valid
        else:
            is_score_valid = True

    # Assigns integer values for each string
    if score == "bogey":
        scores[i] = 1
    elif score == "par":
        scores[i] = 0
    elif score == "birdie":
        scores[i] = -1
    elif score == "eagle":
        scores[i] = -2

# Adds up all the scores
score = sum(scores)

# If score is more than 0 display score over par
if score > 0:
    print(f"\nYour score over {numberOfHoles} holes is {score} over par.")

# If score is less than 0 display score under par
elif score < 0:
    print(f"\nYour score over {numberOfHoles} holes is {abs(score)} under par.")

# If score is 0 display score on par
else:
    print(f"\nYour score over {numberOfHoles} holes is on par.")






