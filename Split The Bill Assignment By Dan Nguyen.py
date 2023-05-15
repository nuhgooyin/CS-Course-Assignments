
##
# Split The Bill Assignment
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/11/27
##

# Initial startup message
print("To get started with splitting your bill, please input the following information.")

# First name
firstName = input("First Name: ")

# Total charge/bill
totalBill = int(input("Enter Total Bill: "))

# Total amount of people to charge/bill
totalPeople = int(input("Enter Number of People: "))

# Percentage to tax
totalTax = int(input("Enter Tax Rate: "))

# Percentage to tip
totalTip = int(input("Enter Tip Percentage: "))

# Calculating tax
finalTax = totalBill / 100 * totalTax

# Calculating tip
finalTip = totalBill / 100 * totalTip

# Calculating subtotal
finalSubTotal = finalTip + finalTax + totalBill

# Calculating tax and tip
finalTipAndTax = finalTip + finalTax

# Calculating final amount one must pay
finalAmountToPay = finalSubTotal / totalPeople

# Final calculated tax
print("\nYour final tax will be: \n" + str(int(finalTax)))

# Final calculated tip
print("Your final tip will be: \n" + str(int(finalTip)))

# Final calculated tax and tip
print("Your final tax and tip will be: \n" + str(int(finalTipAndTax)))

# Final calculated subtotal
print("Your final subtotal will be: \n" + str(int(finalSubTotal)))

# Final calculated amount of money one must pay
print("Each person will have to pay: \n" + str(int(finalAmountToPay)))

# Final ending message
print("\nCongratulations", firstName, "on successfully splitting your bill!")


