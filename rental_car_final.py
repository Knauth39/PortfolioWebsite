import sys
'''
Section 1: Collect customer input
'''

# Rental rates are assigned to three different variables
chargeBudget = 40.00
chargeDaily = 60.00
chargeWeekly = 190.00

# Rental rate variables are assigned to codes - B, D, W
B = chargeBudget
D = chargeDaily
W = chargeWeekly

rentalCode = input("(B)ugdet, (D)aily, or (W)eekly rental?\n").upper()  # The .upper method is included here to avoid error should the user put in a lowercase letter, it will be converted to uppercase
print("You have selected the " + rentalCode + " rate.") # This line is used to ensure the correct rental code has been selected

# Conditional statements based on the rental code input of the user

if rentalCode == 'B':
  print("Enter the number of days Rented:") # Asking user for number of days rented
  rentalPeriod = int(input()) # Accept user input for number of days rented
  print("\nNumber of Days rented: ", rentalPeriod, "\nDaily Budget rate: $", "%.2f" % chargeBudget) # Printing confirmation of number of days rented at the correct rate.  This is to ensure all data is correct and is debugged
elif rentalCode == 'D':
  print("Enter the number of days Rented:") # Asking user for number of days rented
  rentalPeriod = int(input()) # Accept user input for number of days rented
  print("\nNumber of Days rented: ", rentalPeriod, "\nDaily rate: $", "%.2f" % chargeDaily) # Printing confirmation of number of days rented at the correct rate.  This is to ensure all data is correct and is debugged
else: # else statement to account for the selection of weekly rate
  print("Enter the number of weeks Rented:")  # Asking user for number of weeks rented
  rentalPeriod = int(input()) # Accept user input for number of days rented
  print("\nNumber of Weeks rented: ", rentalPeriod, "\nWeekly rate: $", "%.2f" % chargeWeekly) # Printing confirmation of number of days rented at the correct rate.  This is to ensure all data is correct and is debugged

# Using print function to verify data and debug if necessary
if rentalCode == 'B':
  baseCharge = rentalPeriod * chargeBudget
  print("Total rental base charge: $", baseCharge, "\n")
elif rentalCode == 'D':
  baseCharge = rentalPeriod * chargeDaily
  print("Total rental base charge: $", baseCharge, "\n")
else:
  baseCharge = rentalPeriod * chargeWeekly
  print("Total rental base charge: $", baseCharge, "\n")

# Milage calculations and charges
print("Starting Odometer Reading:")
odoStart = int(input()) # Accept user inpur variable as an intege
print("Ending Odometer Reading:")
odoEnd = int(input()) # Accept user inpur variable as an intege

#Calculate total miles driven
totalMiles = odoEnd - odoStart  # Set varibable 'totalMiles' (ending - starting)

print("\nMileage summary\n\nStarting mileage:", odoStart,  "\nEnding mileage: ", odoEnd, "\nTotal mileage: ", totalMiles) # Printing mileage summarty in three lines to verify data and debug if necessary, and to check calculation of totalMiles

# Set three variables which will be used in the conditional statement
# It is important to read and understand these variables, so as to not create repitation in comments below
averageDayMiles = totalMiles / rentalPeriod # Calculates the average DAILY miles driven for the rental period
extraDayMiles = int(averageDayMiles) - 100  # Customer will be charged per mile, if they exceed an average of 100 miles a day for their rental period
averageWeekMiles = totalMiles / rentalPeriod  # Calculates the average WEEKLY miles driven for the rental period
extraWeekMiles = int(averageWeekMiles) - 900  # Customer will be charged per mile, if they exceed an average of 100 miles a day for their rental period

#Conditional statements with nesting
if rentalCode == 'B': # Conditional statement for BUDGET
  mileCharge = totalMiles * .25 # 25 cents is charged for ever mile driven
  print("Budget milage charge total: $", mileCharge)  # Prints the total charged for BUDGET rental to verify data, and debug if necessary
elif rentalCode == 'D': # Or if rental code is DAILY >>>> branched into another conditional statement for different milage calculations
  if averageDayMiles <= 100:  # If average daily miles driven was 100 or less
    mileCharge = 0  # There is no charge on the miles driven
    print("Daily milage charge total: $", mileCharge) # Prints the total charged for DAILY rental to verify data, and debug if necessary
  else: # Or else, if the average daily miles is greater than 100
    mileCharge = extraDayMiles * .25 # Usiing the variable 'extraDailyMiles', $00.25 is charged on every mile over the average 100 miles driven.
    print("Daily milage charge total: $", mileCharge) # Prints the total charged for DAILY rental to verify data, and debug if necessary
else: # Or if rental code is WEEKLY >>>> branched into another conditional statement for different milage calculations
  if averageWeekMiles <= 900: # If average weekly miles driven was 900 or less
    mileCharge = 0 # There is no charge on the miles driven
    print("Weekly milage charge total: $", mileCharge)  # Prints the total charged for WEEKLY rental to verify data, and debug if necessary
  else: # However if the average weekly miles driven exceeds 900 miles >>>> charges below apply
    mileCharge = rentalPeriod * 100.00  # Usiing the variable 'extraWeekMiles', $00.25 is charged on every mile over the average 100 miles driven.
    print("Weekly milage charge total: $", mileCharge)  # Prints the total charged for BUDGET rental to verify data, and debug if necessary

#   Final calculations

amtDue = baseCharge + mileCharge    #   Assigning variable 'amtDue' >>> we gater the data from the baseCharge and add the mileCharge

print("\nRental Summary\n") #   Print 'Rental Summary'
#   This summary prints all the information clearly, using '\n' to break lines
print("Rental Code: ", rentalCode, "\nRental Period: ", rentalPeriod, "\nStarting Odometer: ", odoStart, "\nEnding Odometer: ", odoEnd, "\nMiles Driven: ", totalMiles, "\nAmount Due: $", amtDue)
