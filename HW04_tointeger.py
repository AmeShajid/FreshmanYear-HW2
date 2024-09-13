#Ame Shajid
#Monday April 29, 2024
# OBjective:We are going to write a program that will help us convert binary numbers into decimal
#numbers.




# Define a function to get a valid binary string from the user
def getBinary():
    # We tell the user to input a binary value
    binary_string = input("Enter a Binary Value: ")
    # Get the length of the binary value they gave us
    length = len(binary_string)
    # Check if the input is empty
    if length == 0:
        # If it's empty, print an error message and return False
        print("Invalid Input. Try again.")
        return False
   
    # Initialize an index for iterating through the characters of the input string
    index = 0
    # Iterate through each character of the input string
    while index < length:
        # Get the character at the current index
        char = binary_string[index]
        # Check if the character is not '0' or '1'
        if char != "0" and char != "1":
            # If it's not '0' or '1', print an error message and return False
            print("Invalid Input. Try again.")
            return False
        # Move to the next character by incrementing the index
        index += 1
    
    # If all characters are '0' or '1', return the binary string
    return binary_string

# Define a function to convert a binary string to its integer equivalent
def stringToBinary(binary):
    return int(binary, 2)

#main
if __name__ == "__main__":
    # Print the welcome convertor
    print("Welcome to Binary Converter")
    # Initialize a variable to control the loop so if they press y we keep going
    again = "Y"
    # Start a loop to allow multiple binary conversions
    while again.upper() != "N":
        # Call the getBinary() function to get a valid binary string
        binary = getBinary()
        # Check if getBinary() returns a valid binary string
        if binary:
            # If it's valid, convert the binary string to its integer equivalent
            integer_equivalent = stringToBinary(binary)
            # Print the integer equivalent
            print(f"Integer Equivalent: {integer_equivalent}")
            # Ask the user if they want to convert another binary number
            again = input("Do you want to convert another binary number (Y/N)? ").upper()
    # Print a goodbye message when the loop ends
    print("OK. Good-bye!")








