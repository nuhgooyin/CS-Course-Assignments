##
# Savings Simulator - Initial Release 0.1
#
# @author Dan Nguyen
# @course ICS3UC
# @date 2020/12/08
##

# Starting up message
print("Welcome to savings simulator! To get started, please input the following variables.")

# Getting initial investment variable
initialInvestmentValid = False
while not initialInvestmentValid:
    try:
        print()
        initialInvestment = int(input("Your initial investment: "))

        # Is input a positive integer?
        if (0 < initialInvestment):

            # True break loop
            initialInvestmentValid = True

        # False user input is an integer but is not positive
        else:
            print("\nPlease input positive number.\n")

    # False user input is not an integer type or valid
    except:
        print()
        print("Please input valid information.")

# Final value loop validation
finalValueValid = False
while not finalValueValid:
    # Getting interest rate variable
    interestRateValid = False
    while not interestRateValid:
        try:
            print()
            interestRate = int(input("Interest rate: "))

            # Is input a positive integer?
            if (0 < interestRate):

                # True break loop
                interestRateValid = True

            # False user input is an integer but is not positive
            else:
                print()
                print("Please input positive number.")
                print()

        # False user input is not an integer type or valid
        except:
            print()
            print("Please input valid information.")

    # Getting number of years variable
    numberOfYearsValid = False
    while not numberOfYearsValid:
        try:
            print()
            numberOfYears = int(input("Number of years: "))

            # Is input a positive integer?
            if (0 < numberOfYears):

                # True break loop
                numberOfYearsValid = True

            # False user input is an integer but is not positive
            else:
                print()
                print("Please input positive number.")
                print()

        # False user input is not an integer type or valid
        except:
            print()
            print("Please input valid information.")

    # Setting year number counter to zero
    yearNumberCounter = 0

    # Starting investment calculations message
    print()
    print("Starting investment calculation...")
    print()

    # Begining investment calculations
    yearNumberCounterValid = False
    while not yearNumberCounterValid:

    # Is the year number counter greater than or equal to number of years?
        if (numberOfYears <= yearNumberCounter):

            # True break loop
            yearNumberCounterValid = True

            # Display current investment value before withdrawal
            print()
            print("Your investment value is now", round(initialInvestment,2))

        # False calculate annual interest and value
        else:
            print()
            currentInterestRate = initialInvestment / 100 * interestRate
            initialInvestment = round(currentInterestRate,2) + initialInvestment
            yearNumberCounter += 1

            # Display calculated values to user and round to two decimal places
            print("Year", yearNumberCounter, round(initialInvestment,2))

    # Getting amount to withdraw variable
    amountWithdrawValid = False
    while not amountWithdrawValid:
        try:
            print()
            amountWithdraw = float(input("Amount to withdraw: "))

            # Is input a positive integer?
            if (0 < amountWithdraw):

                # True break loop
                amountWithdrawValid = True

                # Calculating total value after withdrawal
                initialInvestment = initialInvestment - amountWithdraw

            # False user input is an integer but is not positive
            else:
                print()
                print("Please input positive number.")
                print()

        # False user input is not an integer type or valid
        except:
            print()
            print("Please input valid information.")

    # Is investment value more than zero?
    if (initialInvestment > 0):
        finalValueValid = False

    else:
        # Calculate final value
        finalValue = initialInvestment + amountWithdraw

        # Display finalized value
        print()
        print("The finalized value of your investment is:", finalValue)

        finalValueValid = True

