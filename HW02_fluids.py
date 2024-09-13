#Ame Shajid
#April 11,2024
# topic:  asks the user to input a number of fluid ounces , as an integer.
#Allocate the fluid ounces into the various units, first starting with barrels, then gallons, and
#so on, finishing with tablespoons. Then display the results


#this is the introduction where we ask the user how many ounces
fluid_ounces = float(input("How many fluid ounces do you have: "))
# this will display how many ounces they entered also we made it into an integer here so it can show up as an integer
print(f'{int(fluid_ounces)} fluid ounces can be divided into: ')

#honestly I could've put this right underneath the original fluid ounces so i could've just made it print integer fluid ounces but yeah this is what this is
fluid_ounces = int(fluid_ounces)

# these are the conversions for the liquid
barrel = 5376
gallon = 128
quart = 32
pint = 16
cups = 8
gill = 4
ounces = 1
tablespoons = 1

# Calculate the number of barrels
barrel1 = fluid_ounces // barrel
# Calculate the remaining fluid ounces after converting to barrels
fluid_ounces_remainder = fluid_ounces % barrel

# Calculate the number of gallons
gallon1 = fluid_ounces_remainder // gallon
# Calculate the remaining fluid ounces after converting to gallons
fluid_ounces_remainder = fluid_ounces_remainder % gallon

# Calculate the number of quarts
quart1 = fluid_ounces_remainder // quart
# Calculate the remaining fluid ounces after converting to quarts
fluid_ounces_remainder = fluid_ounces_remainder % quart

# Calculate the number of pints
pint1 = fluid_ounces_remainder // pint
# Calculate the remaining fluid ounces after converting to pints
fluid_ounces_remainder = fluid_ounces_remainder % pint

# Calculate the number of cups
cups1 = fluid_ounces_remainder // cups
# Calculate the remaining fluid ounces after converting to cups
fluid_ounces_remainder = fluid_ounces_remainder % cups

# Calculate the number of gills
gill1 = fluid_ounces_remainder // gill
# Calculate the remaining fluid ounces after converting to gills
fluid_ounces_remainder = fluid_ounces_remainder % gill

# Calculate the number of ounces
ounces1 = fluid_ounces_remainder // ounces
# Calculate the remaining fluid ounces after converting to ounces
fluid_ounces_remainder = fluid_ounces_remainder % ounces

# Calculate the number of tablespoons
tablespoons1 = fluid_ounces_remainder // tablespoons

#here we display all the final calculations and conversion stuff
print(f"{barrel1} barrel(s)")
print(f"{gallon1} gallon(s)")
print(f"{quart1} quart(s)")
print(f"{pint1} pint(s)")
print(f"{cups1} cup(s)")
print(f"{gill1} gill(s)")
print(f"{ounces1} ounce(s)")
print(f"{tablespoons1} tablespoon(s)")









