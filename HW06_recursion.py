#Ame Shajid
#May 20, 2024
#The purpose of this homework assignment is to practice algorithm thinking and writing
#and recursive functions.

#** MY FINAL ANSWERS when the run button is pressed it only shows the answer
#Like it said on the homework.
#I did not include the test cases in the final answers because it was not asked for
#the question was just asking for the answer
#so I only told my code to print the answer
#for the test cases I also commented how it works and what it should return



#BC = Base Case
#RC = Recursive Case

# Part 1: The Dot Product

def dotProduct(list1, list2):
    # BC: if the lists are not of the same length, return 0.0
    if len(list1) != len(list2):
        return 0.0
    
    # BC: if both lists are empty, return 0.0
    if len(list1) == 0:
        return 0.0
    
    # RC: multiply the first elements and add to the dot product of the rest
    return list1[0] * list2[0] + dotProduct(list1[1:], list2[1:])

# Test cases for dotProduct
print(dotProduct([5, 3], [6, 4]))  # Should return 42.0 (5*6 + 3*4)
print(dotProduct([1, 2, 3, 4], [10, 20, 30, 50]))  # Should return 340.0 (1*10 + 2*20 + 3*30 + 4*50)
print(dotProduct([5, 3], [6]))  # Should return 0.0 (lists are of different lengths)
print(dotProduct([], [15]))  # Should return 0.0 (one list is empty)
print(dotProduct([], []))  # Should return 0.0 (both lists are empty)

# Part 2: Finding elements

def findPosition(container, element, index=0):
    # BC: if index reaches the length of the container, return the length of the container
    if index == len(container):
        return len(container)
    
    # BC: if the element at the current index matches the element we are looking for, return the index
    if container[index] == element:
        return index
    
    # RC: check the next index
    return findPosition(container, element, index + 1)

# Test cases for findPosition
print(findPosition([55, 77, 42, 12, 42, 100], 42))  # Should return 2 (first occurrence of 42 is at index 2)
print(findPosition(list(range(0, 100)), 42))  # Should return 42 (element 42 is at index 42)
print(findPosition(['hello', 42, True], 'hi'))  # Should return 3 (element 'hi' is not in the list, so return length of list)
print(findPosition(['well', 'hi', 'there'], 'hi'))  # Should return 1 (element 'hi' is at index 1)
print(findPosition('team', 'i'))  # Should return 4 (element 'i' is not in the string, so return length of string)
print(findPosition('Outer Exploration', ' '))  # Should return 5 (first space is at index 5)
print(findPosition('Outer Exploration', 'U'))  # Should return 17 (element 'U' is not in the string, so return length of string)

# Part 3: The Collatz sequence

def maxCollatz(number):
    # BC: if the number is 1, return 1 since it's the end of the sequence
    if number == 1:
        return 1
    
    # RC: compute the next number in the Collatz sequence and get its maximum value
    if number % 2 == 0:
        next_number = number // 2
    else:
        next_number = number * 3 + 1
    
    # RC: find the maximum in the rest of the sequence
    max_in_rest = maxCollatz(next_number)
    
    # Return the maximum value between the current number and the maximum of the rest of the sequence
    return max(number, max_in_rest)

# Test cases for maxCollatz
print(maxCollatz(10))  # Should return 16 (sequence: 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, maximum is 16)
print(maxCollatz(32))  # Should return 32 (sequence: 32 -> 16 -> 8 -> 4 -> 2 -> 1, maximum is 32)
print(maxCollatz(85))  # Should return 256 (sequence has maximum value 256)
print(maxCollatz(33))  # Should return 100 (sequence has maximum value 100)
print(maxCollatz(7))   # Should return 52 (sequence has maximum value 52)
print(maxCollatz(25))  # Should return 88 (sequence has maximum value 88)










