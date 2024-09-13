#Ame Shajid
#April 11,2024
#topic: We are going to write a program that calculates the distance from the Earth to the Sun, on
#any given day. The Earth's orbit is elliptical, and the distance of the Earth from the Sun can

#we import math so we can use the math functions
import math

#ill leave these here because we are going to need these for the function ill leave it gloval for now
axis = 149600000
eccentricity = 0.0167

# Function to calculate the angle from perihelion given the number of days
def calculateAngleFromPerihelion(days):
    # Calculate the angle using the formula
    distance =  (2 * math.pi * days) / 365.256
    return distance

# Function to calculate the distance from the Sun given the angle from perihelion
def calculateDistanceFromSun(omega): 
    # Define constants within the function (not necessary since they're already defined globally)
    axis = 149600000 
    eccentricity = 0.01672
    # Calculate the distance using the  formula
    distance = axis * (1 - math.pow(eccentricity, 2)) / (1 + eccentricity * math.cos(omega))
    return distance

# Main script
if __name__ == "__main__": #we are running this first
    # Prompt the user to enter the number of days from perihelion and convert it to an integer
    days = int(input("Enter the number of days from perihelion: "))
    
    # Calculate the angle from perihelion using the provided function
    omega = calculateAngleFromPerihelion(days)
    
    # Calculate the distance from the Earth to the Sun
    distance_km = calculateDistanceFromSun(omega)
    
    # Convert the distance from kilometers to miles
    distance_miles = distance_km * 0.6215
    
    # we will print everything here
    print(f"On this day the distance from the Earth to the Sun is {distance_km:.2f} km")
    print(f"That is {distance_miles:.2f} miles")











