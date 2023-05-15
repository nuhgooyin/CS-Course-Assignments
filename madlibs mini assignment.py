
##
# Mad Libs Assignment
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/11/24
##

# Get 9 input variables for the story
Name = input("Name: ")

Age = input("Age: ")

Verb_with_ing = input("Verb with ing: ")

Place = input("Place: ")

Time = input("Time: ")

Noun = input("Noun: ")

Verb = input("Verb: ")

Mood = input("Mood: ")

Medical_condition = input("Medical condition: ")

# The pregenerated story incorporated with the input variables
print(Name, "was walking over to", Place, "at around", Time+ ".", end="")

print(Name, "was", Verb, "over to", Noun+ ".")

print(Name, "is", Age, "years old, and therefore prone to a terminal illness.")

print(Name, "is", Mood, "because of this recent medical diagnosis of", Medical_condition)