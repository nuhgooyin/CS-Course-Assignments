
##
# Password Generator - Initial Release Version 0.1
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/11/26
##

# Initial startup message
print("Let's get you started on creating your very own custom and secure password! Please input the following information.")

# Full name of user
firstName = input("First Name: ")

lastName = input("Last Name: ")

# Current age of user
age = int(input("Age: "))

result1 = age - 3

# Location of birth
locationOfBirth = input("Location of Birth: ")

# Name of family member
familyMemberName = input("Name of Family Member: ")

# Car brand
carBrand = input("Car Brand: ")

# Phone brand
phoneBrand = input("Phone Brand: ")

# Favorite sports team
favoriteSportsTeam = input("Favorite Sports Team: ")

# House
houseNumber = int(input("House Number: "))

result2 = houseNumber - 5

# Generating final custom password
password = [""]

password.append (firstName[0:len(firstName) // 2]) # Takes first letter to the middle
password.append (lastName[len(lastName) // 2::].upper()) # Takes middle to last letter and makes it upper case
password.append (str(abs(result1))) # Takes absolute value of result1
password.append (locationOfBirth[0:3]) # Takes first three characters
password.append (familyMemberName[:2]) # Takes first two chracters
password.append (carBrand[0:len(carBrand) // 2])
password.append (phoneBrand[-1]) # Takes last character
password.append (favoriteSportsTeam[0]) # Takes first character
password.append (str(abs(result2)))

passwordString = "".join(password) # Converts the password list into string


# Final generated custom and secure password
print("Your custom and secure password is: " + passwordString)

