#Ame Shajid
#Date: April 20, 2024
#Assignment: Homework 3
#The purpose of this homework assignment is to practice algorithm thinking and writing
#a program that uses basic input / output, variables, conditional branching, and
#programmer defined functions.


#Note I used the .lower function and I lowkey am not sure if they taught that in class, I took this class last term so i kind of used it, but if I didn't use it I wouldve changed the def monthtonumber and had to have added all three version, but at the same time there are lots of possibilites so idk how else we would do it wihtout using the .lower or .upper function

def monthToNumber(abbreviation):
    # basically what this does is take the abbreviation and then makes it into the months and then returns the months we input with a number
    if abbreviation == 'jan':
        return 1
    elif abbreviation == 'feb':
        return 2
    elif abbreviation == 'mar':
        return 3
    elif abbreviation == 'apr':
        return 4
    elif abbreviation == 'may':
        return 5
    elif abbreviation == 'jun':
        return 6
    elif abbreviation == 'jul':
        return 7
    elif abbreviation == 'aug':
        return 8
    elif abbreviation == 'sep':
        return 9
    elif abbreviation == 'oct':
        return 10
    elif abbreviation == 'nov':
        return 11
    elif abbreviation == 'dec':
        return 12
    else:
        print("Invalid Month")  # Print a message if the abbreviation is not recognized
        return 0  # Return 0 to indicate an invalid month


def IsValidDate(month, day):
    # This function checks if a given day is valid for the given month.
    # It returns True if the day is valid, False otherwise.
    # It accounts for the varying number of days in each month.
    if month == 1:
        return 1 <= day <= 31
    elif month == 2:
        return 1 <= day <= 29  # February can have up to 29 days in a leap year
    elif month == 3:
        return 1 <= day <= 31
    elif month == 4:
        return 1 <= day <= 30
    elif month == 5:
        return 1 <= day <= 31
    elif month == 6:
        return 1 <= day <= 30
    elif month == 7:
        return 1 <= day <= 31
    elif month == 8:
        return 1 <= day <= 31
    elif month == 9:
        return 1 <= day <= 30
    elif month == 10:
        return 1 <= day <= 31
    elif month == 11:
        return 1 <= day <= 30
    elif month == 12:
        return 1 <= day <= 31
    else:
        return False  # Return False for invalid months


def getTamilSeason(month, day):
    # This function returns the Tamil season based on the given month and day.
    # Each season corresponds to a specific range of dates in the Tamil calendar.
    if not IsValidDate(month, day):
        return "Day Invalid"  # If the day is not valid, return a message
    
    # The following series of conditions determine the Tamil season based on the month and day.
    # Each season has its specific range of dates.



    #I spaced mine out into interval of threes because each month has a three month pattern
    
    if month == 4 and 15 <= day <= 30:
        return "MuthuVenil"
    elif month == 5 and 1 <= day <= 31:
        return "MuthuVenil"
    elif month == 6 and 1 <= day <= 14:
        return "MuthuVenil" 
    
    elif month == 6 and 15 <= day <= 30:
        return "Kaar"
    elif month == 7 and 1 <= day <= 31:
        return "Kaar"
    elif month == 8 and 1 <= day <= 14:
        return "Kaar" 
   
    elif month == 8 and 15 <= day <= 31:
        return "Kulir"
    elif month == 9 and 1 <= day <= 30:
        return "Kulir"
    elif month == 10 and 1 <= day <= 14:
        return "Kulir" 
    
    elif month == 10 and 15 <= day <= 31:
        return "MunPani"
    elif month == 11 and 1 <= day <= 30:
        return "MunPani"
    elif month == 12 and 1 <= day <= 14:
        return "MunPani" 

    elif month == 12 and 15 <= day <= 31:
        return "PinPani"
    elif month == 1 and 1 <= day <= 30:
        return "PinPani"
    elif month == 12 and 1 <= day <= 14:
        return "PinPani"

    elif month == 2 and 15 <= day <= 29:
        return "IlaVenil"
    elif month == 3 and 1 <= day <= 31:
        return "IlaVenil"
    elif month == 4 and 1 <= day <= 14:
        return "IlaVenil"
    else:
        return "Invalid Month"  # If the month is not recognized, return an error message


if __name__ == "__main__":
    # tells the user to input a month and day, then calculates and prints the corresponding Tamil season.
    month = input("Enter Month (three letter abbreviation): ").lower()
    month_number = monthToNumber(month)

#we need a nested if else beacuse once we check for our months then we want to make sure it checks for days and it isn't just repeated
    if month_number == 0:  # Check if the month abbreviation is invalid
        print("Good-bye!")  # If so, print a goodbye message
    else:
        day = int(input("Enter Day (number): "))  # Prompt the user to input the day
        if not IsValidDate(month_number, day):  # Check if the day is invalid for the given month
            print("Invalid Day")  # If so, print an error message
            print("Good-bye!")  # Print a goodbye message
        else: # final part to calculate
            season = getTamilSeason(month_number, day)  
            print("Tamil Season is", season)  


