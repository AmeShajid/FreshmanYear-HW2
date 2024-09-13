#Ame Shajid
#Monday April 29, 2024
# Objective : The purpose of this homework assignment is to practice algorithm thinking and writing
#a program that uses basic input / output, variables, conditional branching, while
#loops, strings, and programmer defined functions.



def daysToDistance(initialDistance, goalDistance):
    # over here we are getting the string input from our main function and checking if we entered numbers
    if str(initialDistance).isdigit() and str(goalDistance).isdigit():
        # once we know we got numbers we Convert them to integers
        initialDistance = int(initialDistance)
        goalDistance = int(goalDistance)
        # then we have to make sure both our distances are positive integers
        if initialDistance > 0 and goalDistance > 0:
            # now here our current distance is equal to our initial distance
            currentDistance = initialDistance
            days = 0
            # Increase distance by 10% each day until goal distance is reached or exceeded
            while currentDistance < goalDistance:
                currentDistance *= 1.1
                days += 1
            # Add 1 to account for the initial day 
            #right here I kept getting one day less until i realzied I wasn't accounting for the first day
            return days + 1
        else:#and ya these two
            return "Invalid input. Distance values must be positive integers."
    else:
        return "Invalid input. Please enter integers."


if __name__ == "__main__":
    print("Training Days Calculator")

    # so here is just the while loop that checks for my initial distance and like validates everything
    initialDistance = 0
    while initialDistance <= 0:
        initialDistance = input("Enter initial distance in miles: ")
        # Validate user input for initial distance
        if initialDistance.isdigit():
            initialDistance = int(initialDistance)
            if initialDistance <= 0:
                print("Invalid input. Please try again.")
                initialDistance = 0
        else:
            print("Invalid input. Please try again.")
            initialDistance = 0

    # Get goal distance from user
    goalDistance = 0
    while goalDistance <= 0:
        goalDistance = input("Enter goal distance in miles: ")
        # Validate user input for goal distance
        if goalDistance.isdigit():
            goalDistance = int(goalDistance)
            if goalDistance <= 0:
                print("Value is too low. Please try again.")
                goalDistance = 0
        else:
            print("Invalid input. Please try again.")
            goalDistance = 0

    # Calculate the number of days required to reach the goal distance
    days_required = daysToDistance(initialDistance, goalDistance)

    # Print the result
    print(f"You will need {days_required} days to achieve your goal.")









