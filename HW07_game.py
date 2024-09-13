#Ame Shajid
#May 28,2024
#The purpose of this homework assignment is to practice algorithm thinking ,
#incremental development, and writing functions.



# First, we import the randint function from the random module
from random import randint

# This function checks for the sum of all dice in myList that match the goal value
def checkSingles(myList, goal):
    total = 0
    for x in myList:  # Loop through each value in the list
        if x == goal:  # If the value matches the goal
            total += x  # Add the value to the total
    return total  # Return the sum of the matching values


#The next three functinos should be the same?


# This function checks if there are at least three of the same value in the list
def checkThreeOfKind(myList):
    for value in myList:  # Loop through each value in the list
        if myList.count(value) >= 3:  # Check if the value appears at least three times
            return 30  # If so, return a score of 30
    return 0  # Otherwise, return 0

# This function checks if there are at least four of the same value in the list
def checkFourOfKind(myList):
    for value in myList:  # Loop through each value in the list
        if myList.count(value) >= 4:  # Check if the value appears at least four times
            return 40  # If so, return a score of 40
    return 0  # Otherwise, return 0

# This function checks if there are at least five of the same value in the list
def checkFiveOfKind(myList):
    for value in myList:  # Loop through each value in the list
        if myList.count(value) >= 5:  # Check if the value appears at least five times
            return 50  # If so, return a score of 50
    return 0  # Otherwise, return 0




# This function checks if the list represents a full house (three of one value and two of another)
def checkFullHouse(myList):
    unique_values = []  # Create an empty list to store unique values
    for value in myList:  # Loop through each value in the list
        if value not in unique_values:  # If the value is not already in unique_values
            unique_values.append(value)  # Add the value to unique_values
    
    if len(unique_values) == 2:  # If there are exactly two unique values
        for value in unique_values:  # Loop through the unique values
            if myList.count(value) in [2, 3]:  # Check if one value appears 2 times and the other 3 times
                return 35  # If so, return a score of 35
    return 0  # Otherwise, return 0

# This function checks if the list contains a straight of four consecutive numbers
def checkStraight(myList):
    if len(myList) < 4:  # If the list has fewer than 4 items, return 0
        return 0
    
    sorted_list = sorted(myList)  # Sort the list to make it easier to find consecutive numbers
    for i in range(len(sorted_list) - 3):  # Loop through the list up to the fourth-to-last item
        if (sorted_list[i + 1] == sorted_list[i] + 1 and 
            sorted_list[i + 2] == sorted_list[i] + 2 and 
            sorted_list[i + 3] == sorted_list[i] + 3):  # Check if four consecutive numbers are found
            return 45  # If so, return a score of 45
    return 0  # Otherwise, return 0



#code will be same for each category copy and paste


# This function finds the highest possible score for a given list of dice
def findHighScore(myList):
    max_score = 0  # Initialize max_score to 0
    max_category = ""  # Initialize max_category to an empty string
    for i in range(1, 7):  # Loop through each possible die value (1 through 6)
        singles_score = checkSingles(myList, i)  # Calculate the score for singles of this value
        if singles_score > max_score:  # If this score is higher than the current max_score
            max_score = singles_score  # Update max_score
            max_category = "Singles"  # Update max_category
    
    three_of_kind_score = checkThreeOfKind(myList)  # Check for a three of a kind
    if three_of_kind_score > max_score:  # If this score is higher than the current max_score
        max_score = three_of_kind_score  # Update max_score
        max_category = "Three Of A Kind"  # Update max_category
    
    four_of_kind_score = checkFourOfKind(myList)  # Check for a four of a kind
    if four_of_kind_score > max_score:  # If this score is higher than the current max_score
        max_score = four_of_kind_score  # Update max_score
        max_category = "Four Of A Kind"  # Update max_category
    
    five_of_kind_score = checkFiveOfKind(myList)  # Check for a five of a kind
    if five_of_kind_score > max_score:  # If this score is higher than the current max_score
        max_score = five_of_kind_score  # Update max_score
        max_category = "Five Of A Kind"  # Update max_category
    
    full_house_score = checkFullHouse(myList)  # Check for a full house
    if full_house_score > max_score:  # If this score is higher than the current max_score
        max_score = full_house_score  # Update max_score
        max_category = "Full House"  # Update max_category
    
    straight_score = checkStraight(myList)  # Check for a straight
    if straight_score > max_score:  # If this score is higher than the current max_score
        max_score = straight_score  # Update max_score
        max_category = "Straight"  # Update max_category
    
    return [max_score, max_category]  # Return the highest score and its category

# This function rolls five dice and returns the results as a list
def roll_dice():
    results = []  # Create an empty list to store the dice results
    for _ in range(5):  # Loop five times (once for each die)
        roll = randint(1, 6)  # Roll a die (generate a random number between 1 and 6)
        results.append(roll)  # Add the result to the list
    return results  # Return the list of results

# This function displays the player's number, their dice rolls, their highest score, and the category
def display_player(player_num, dice, score, category):
    print(f"Player {player_num}")  # Print the player's number
    print("--------")  # Print a separator line
    for i in range(len(dice)):  # Loop through each die roll
        print(f"Dice {i+1}: {dice[i]}")  # Print the die number and its result
    print(f"Category: {category}")  # Print the category of the highest score
    print(f"High score: {score}")  # Print the highest score

# This function determines and prints the winner based on the scores and categories of both players
def determine_winner(player1_score, player1_category, player2_score, player2_category):
    if player1_score > player2_score:  # If player 1's score is higher
        print("---------------")
        print("Player 1 wins!")  # Print that player 1 wins
    elif player2_score > player1_score:  # If player 2's score is higher
        print("---------------")
        print("Player 2 wins!")  # Print that player 2 wins
    else:  # If both scores are equal
        print("--------------")
        print("It's a tie!")  # Print that it's a tie

# This block runs when the script is executed directly
if __name__ == "__main__":
    
    player1_dice = roll_dice()  # Roll dice for player 1
    player1_score, player1_category = findHighScore(player1_dice)  # Find the highest score and category for player 1
    display_player(1, player1_dice, player1_score, player1_category)  # Display player 1's results

    player2_dice = roll_dice()  # Roll dice for player 2
    player2_score, player2_category = findHighScore(player2_dice)  # Find the highest score and category for player 2
    display_player(2, player2_dice, player2_score, player2_category)  # Display player 2's results

    determine_winner(player1_score, player1_category, player2_score, player2_category)  # Determine and print the winner
