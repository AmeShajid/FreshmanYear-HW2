#Ame Shajid
#June 3, 2024
#The purpose of this homework assignment is to practice algorithm thinking ,
#nderstanding and implementing sorting algorithms


#ALSO The homework says:
""" 
For this assignment you must submit your source code, that is your .py files:
HW07_sort.py a single file.

I named my file HW07 and not hw08 because the homework says HW07_sort.py
"""
# auxiliary means like tempory lists to help us sort the main list so thats why i named it aux list



import random  # I'm importing the random module to generate random numbers for the list.

def newSort(numbers):
    if not numbers:  # If the list is empty, I immediately return an empty list.
        return []

    # Find the maximum value in the list to determine the number of digits in the largest number.
    max_val = max(numbers)
    max_digits = len(str(max_val))  # Convert the maximum value to a string to count its digits.

    # I iterate over each digit place: units (0), tens (1), hundreds (2), etc.
    for digit_place in range(max_digits):
        # Create 10 auxiliary lists (one for each digit 0-9) for the current digit place.
        aux_lists = [[] for _ in range(10)]

        # I place each number in the appropriate auxiliary list based on the current digit place.
        for number in numbers:
            digit = (number // (10 ** digit_place)) % 10  # Extract the current digit.
            aux_lists[digit].append(number)  # Append the number to the corresponding auxiliary list.

        # Flatten the auxiliary lists back into the original list while preserving the order.
        numbers = [num for sublist in aux_lists for num in sublist]

    return numbers  # Return the sorted list.

if __name__ == "__main__":
    num_values = None
    while num_values is None:  # I start a loop to continuously prompt the user until valid input is received.
        try:
            num_values_input = int(input("How many values do you want in the list? "))  # Ask for the number of values.
            if num_values_input > 0:  # Check if the number is positive.
                num_values = num_values_input
            else:
                print("Error: you must enter a positive value.")
        except ValueError:  # Handle non-integer inputs.
            print("Invalid input. Please try again.")

    min_value = None
    while min_value is None:  # Another loop for the minimum value input.
        try:
            min_value_input = int(input("What should be the minimum value? "))  # Ask for the minimum value.
            min_value = min_value_input  # Exit the loop if the input is valid.
        except ValueError:  # Handle non-integer inputs.
            print("Invalid input. Please try again.")

    max_value = None
    while max_value is None:  # Loop for the maximum value input.
        try:
            max_value_input = int(input("What should be the maximum value? "))  # Ask for the maximum value.
            if max_value_input > min_value:  # Check if the maximum is greater than the minimum.
                max_value = max_value_input
            else:
                print(f"Error: you must enter a value greater than {min_value}")
        except ValueError:  # Handle non-integer inputs.
            print("Invalid input. Please try again.")

    # Generate a list of random integers between the specified minimum and maximum values.
    numbers = [random.randint(min_value, max_value) for _ in range(num_values)]

    print(f"Before: {numbers}")  # Display the original, unsorted list.
    sorted_numbers = newSort(numbers)  # Call the newSort function to sort the list.
    print(f"After: {sorted_numbers}")  # Display the sorted list.

