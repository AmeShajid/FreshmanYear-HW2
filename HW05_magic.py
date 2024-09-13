#Ame Shajid

#May 6th 2024

#The purpose of this homework assignment is to practice algorithm thinking and writing
#a program that uses basic input / output, integers, Python lists, conditional branching,
#while and for loops, and programmer defined functions.

#matrix = [3,3] i used the term matrix to represent the square




# NOTICE: while solving this problem, you may find the need to create one or more helper
#functions (for example to validate user input). That is fine and you can add those
#functions to your program.

#I created 2 exttra functions:
#def getSquareValues(size): checks for the values in the square
#def isValueInSquare(square, value): checks if the value is in the square

#I did these two in 2 different functions because I wanted to make sure that the values were correct and that they were not already in the square
#It was easier to make extra fucntiosn to check

# Function to make a square matrix with zeros
def populateSquare(size):
    square = []
    # Loop through rows
    for i in range(size):
        row = []
        # Loop through columns
        for j in range(size):
            row.append(0)  # Append zero to each column
        square.append(row)  # Append row to the square
    return square

# Function to print the square matrix
#basic code to just make a literal square
def printSquare(square):
    # Loop through rows
    for row in square:
        # Loop through elements in the row
        for element in row:
            print(element, end=' ')  # Print each one followed by a space
        print()  # Move to the next line after printing each row


# Function to check if a square matrix is a magic square
# this functions is basically the math part and the validating part
def isMagicSquare(square):
    n = len(square)  # Get the size of the square
    magicSum = n * (n ** 2 + 1) / 2  # Calculate the magic sum
    
    # Check each row sum
    for row in square:
        if sum(row) != magicSum:  # If row sum is not equal to magic sum
            return False  # Not a magic square
    
    # Check each column sum
    for i in range(n):
        col_sum = 0
        for row in square:
            col_sum += row[i]
        if col_sum != magicSum:  # If column sum is not equal to magic sum
            return False  # Not a magic square
    
    # Check diagonal sums
    diagonal_sum1 = 0
    for i in range(n):
        diagonal_sum1 += square[i][i]
    if diagonal_sum1 != magicSum:  # If diagonal sum is not equal to magic sum
        return False  # Not a magic square
    
    diagonal_sum2 = 0
    for i in range(n):
        diagonal_sum2 += square[i][n - i - 1]
    if diagonal_sum2 != magicSum:  # If diagonal sum is not equal to magic sum
        return False  # Not a magic square
    
    return True  # If all conditions passed, it's a magic square if not then nope

# Function to get values for the square matrix from user input
def getSquareValues(size):
    square = populateSquare(size)  # make the square with zeros
    for i in range(size):
        print("Row", i + 1) # this will keep asking for the rows
        for j in range(size):
            value = 0
            invalid_input = True
            # Keep asking for input until valid input is provided
            while invalid_input:
                value_input = input("Enter a value for the square: ")
                if value_input.isdigit():  # Check if input is a digit
                    value = int(value_input)
                    # Check if value is within bounds and not already in the square
                    if 1 <= value <= size ** 2 and not isValueInSquare(square, value):
                        invalid_input = False  # Valid input, exit loop
                    else:#these are jsut error mesasages
                        if isValueInSquare(square, value):
                            print("Error: this value already exists in the square. Enter a different value.")
                        else:
                            print("Value out of bounds. Please try again.")
                else:
                    print("Invalid input. Please try again.")  # If input is not a digit
            square[i][j] = value  # Assign the validated value to the square
    return square

# Function to check if a value already exists in the square
def isValueInSquare(square, value):
    for row in square:
        if value in row:
            return True  # Value found in a row, return True
    return False  # Value not found in the square

# Main program
if __name__ == '__main__':
    print("Welcome to the Magic Square Game")
    size = 0
    # Get size of the square from user input
    size_input = input("Enter the size of your square (between 3 and 9): ")
    while not (size_input.isdigit() and 3 <= int(size_input) <= 9):
        if size_input.isdigit():
            print("Value out of bounds. Please try again.")
        else:
            print("Invalid input. Please try again.")
        size_input = input("Enter the size of your square (between 3 and 9): ")
    size = int(size_input)
    
    square = getSquareValues(size)  # Get values for the square
    print()
    print("Here is your square:")
    printSquare(square)  # Print the square
    if isMagicSquare(square):
        print("This is a magic square!!")  # Check if it's a magic square
    else:
        print("This is not a magic square.")








