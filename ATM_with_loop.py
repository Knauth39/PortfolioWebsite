import sys

# -------------------------- DECLARE variables for balance, deposit, and withdrawal --------------------------

account_balance = float(500.25)                                                 # Starting balance indicated by Codio
#balance = 100
amount = 0
#deposit_amount = 0                                                              # Declare variable 'deposit_amount'
#withdrawal_amount = 0                                                           # Declare variable 'withdrawal_amount'
pin = ''

# -------------------------- DEFINE FUNCTIONS - balance, withdrawal, and deposit -----------------------------
def transactionGo (pin):
  pin = int(input("Please enter your 5 digit pin number:\n"))

  def balance(account_balance):                                                   # Define balance function
    print("Your current balance is $%.2f" % (account_balance))                    # Prints the current avalible balance

  def deposit(account_balance, amount):                                           # Define DEPOSIT function with parameters account_balance and amount
    amount = float(input("How much would you like to deposit today?\n"))          # Accept user input for the deposit amount, in float format
    balance = account_balance + amount                                            # This addition assigns the updated value of the account blance, to the variable 'account_balance'
    print("Deposit was $%.2f , your new current balance is $%.2f" % (amount, balance))  # Prints depost amount and account balance
    return balance                                                                # Return records the new value of account_balance to reflect accordingly in other transactions


  def withdrawal(account_balance, amount):                                        # Define WITHDRAWAL function with parameters account_balance and withdrawal_amount
    amount = float(input("How much would you like to withdraw today?\n"))         # Accept user input for the withdrawal amount, in float format
    if amount > account_balance:                                                  # Checking to see if the amount requested, is greater than the amount avalible
      print("Insuffient funds, $%.2f is greater than your account balance of $%.2f" % (amount, account_balance)) # If the amount requested is greater than the account balance, there are insuffient funds
    else:                                                                         # Suffient amount of funds are avalible, the function continues
      balance = account_balance - amount                                          # Variable 'balance' is assigned to reflect the new avalible balance
      print ("Withdrawal amount was $%.2f, your new current balance is $%.2f" % (amount, balance))  # Prints withdrawal amount and account balance
      return balance                                                              # Return records the new value of balance to reflect accordingly in other transactions

# Lines 18 and 20 compose a conditional statement with the withdrawal function
# Line 18 => if the requested withdwal amount is greater than the account balance, the conditional statement stops, and prints to the user there are insuffient funds
# Line 20 => if there are Suffient funds avalible, the conditional statement continues, updates the 'balance', and outputs to the user their withdwal amount and new avalible balance

# ------------------------------------ ACCEPT USER INPUT - D, B, W, or Q -------------------------------------
userAccess = input ("Welcome to Tom & Kate Banking, if you would like to sign into your account, please press (C)ontinue, or (E)xit\n").upper()
if userAccess == 'C':
  transactionGo (pin)

  userChoice = 'go'                                                               # Setting the variable 'userChoice' to 'go', so we can impliment a while loop

  # Step ONE => Create a WHILE loop to offer the user additional options after they have completed a transation
  while userChoice != 'E':                                                        # As long as the user does not select 'E' (Exit), the program will keep looping with user choices

  # Step TWO =>  Ask user what action they would like to proceed with, user input is accepted and assigned to the variable 'userchoice'
    userChoice = input ("Would you like to check your (B)alance, make a (D)eposit, (W)ithdraw cash, or (E)xit?\n").upper()

  # Step THREE => conditional statement begins based on the value of variable 'userchoice' from user input
  # Four branches ustilizing if / elif for DEPOSIT, BALANCE, WITHDRAWAL, EXIT
    if (userChoice == 'D'):                                                       # Accepts input D and proceeds with function 'deposit'
      deposit (account_balance, amount)                                           # DEPOSIT function is called with parameters 'balance' and 'amount'

    elif (userChoice == 'B'):                                                     # Accepts input B and proceeds with function 'balance'
      balance (account_balance)                                                   # BALANCE function is called with parameter 'balance'

    elif (userChoice == 'W'):                                                     # Accepts input D and proceeds with function 'withdrawal'
      withdrawal (account_balance, amount)                                        # WITHDRAWAL function is called with parameters 'balance' and 'amount'

    elif (userChoice == 'E'):                                                     # Accepts input E for EXIT
      print("Thank you for banking with us.")                                     # There is no function for EXIT, and therefore the user has a printed message ending their session

else:
  print("We hope to see you again soon, have a nice day!")
