import sys

# -------------- List of variables for quick and clear reference ---------------
# grocery_item = dictionary
# grocery_history = list
# item_total = item's price * item's quantity
# grand_total = total of all purchased items
# item_name = name of grocery item purchased
# quantity = how many grocery items are purchased
# cost = how much the single item costs
# name = diction key for item_name
# number = dictionary key for quantity
# price = dictionary key for cost

# ------------------------- Define dictionary and list -------------------------
grocery_item = {}                                           # Defines (creates) the empty dictionary using curly brackets {}
grocery_history = []                                        # Defines (creates) the empty list using square brackets []

stop = 'go'                                                 # Variable used to check if the while loop condition is met

while stop != 'q':                                          # Create the while loop for user input to collect data, as long as 'stop' does not equal 'q'
  item_name = input("Item name:\n")                         # Accepting input for the name of the item being purchased
  quantity = input("Quantity purchased:\n")                 # Accepting input for the price of the item being purchased
  cost = input("Price per item:\n")                         # Accepting input for the number of items being purchased

# ----------------- Add values to the dictionary grocery_item ------------------
  grocery_item['name'] = item_name                          # This is a string
  grocery_item['number'] = int(quantity)                    # This is an integer
  grocery_item['price'] = float(cost)                       # This is a float, because it may be a decimal

# ---------------- Adding the dictionary to the list created -------------------
  grocery_history.append({'name':item_name, 'number':int(quantity), 'price':float(cost)})
# Here we accept input from the user to either continue the loop and add more items, or exit the loop and print the totals
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

# ----------------------------- Final calculations -----------------------------
grand_total = 0                                             # Declare the variable grand_total and set to 0

for index, item in enumerate(grocery_history):              # The enumerate function will loop over with an automatic counter accessing the index
  item_total = item['number'] * item['price']               # Calulate the price of an item, considering the quanity and unit cost, not to be printed using "number * price"
  grand_total += item_total                                 # Calculate the grand_total of all items putchsed, using a compound operator to keep simple and short

  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
# The above function I used % as placeholders to simplify formating for ints and strings, also for the purpose of setting to two decimal places representing cents in the money format.
  item_total = 0

print('Grand total: $%.2f' % grand_total)                   # Prints total cost of the entire grocery list
