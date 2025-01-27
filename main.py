#*****************************************************************************
# Author:           GD Iyer
# Lab:              (fill in with Lab 1, etc.)
# Date:             (fill in)
# Description:      This program will read principal, rate and time and 
#                   calculate the simple interest for that amount.
# Input:            (What the program asks for, and the data type, e.g. string)
# Output:           (Summary of messages displayed by the program)
# Sources:          Lab 1 specifications
#                   and any other substantial aids, like web pages or students
#                   who helped you.
#*****************************************************************************
# Neither comments nor code should be wider than 79 characters.
# The lines of asterisks above are 79 characters long for easy reference.

#constants - None here

#main() function
def main():
  #print welcome message
  print("Welcome to my Multi-Option Calculator!!")
  print()
  
  #declare all variables here
  option = ""
  principal = 0.0
  rate = 0.0
  period = 0
  interest = 0.0
  totalAmount = 0.0
  numMonths = 0
  monthlyPayment = 0.0

  #display prompts or menu and read input
  print("Please pick an option from below: ")
  print("(S) Simple Interest")
  print("(A) Auto Loan")
  option = input('>>')
  option = option.upper()  #convert to upper case before checking.

  #conditional statements for the different options.
  #if option is S - since we converted to uppercase
  if option == 'S':
    #user input
    principal = float(input("\nEnter the principal amount: $"))
    rate = float(input("Enter the rate in percentage: "))
    period = int(input("Enter the period in years: "))

    #calculations for simple interest
    interest = principal * (1 +((rate / 100) * period)) - principal
    totalAmount = principal + interest

    #output to user
    print("\nYour interest accrued is $", (format(interest, '.2f')))
    print("Your total amount with interest is $", (format(totalAmount, '.2f')))
    print("Thank you for using my interest calculator")
    
  #else if option is A - since we converted to uppercase
  elif option == 'A':
    #user input
    principal = float(input("\nEnter the price of the car: $"))
    rate = float(input("Enter the rate in percentage: "))
    numMonths = int(input("Enter the number of monthly payments: "))
    
    #monthly payment calculations
    rate = rate / 100;
    monthlyPayment = (principal * (rate / 12)) / (1 - pow((1 + rate / 12), (-1 * numMonths)))
    
    #output to user
    print("\nYour total monthly payment is $", (format(monthlyPayment, '.2f')))
    print("Thank you for using my Auto Loan calculator!!")

  #else if neither S nor A, invalid option
  else:
    print("Invalid option!! Please try again later!")
    
#call main
main()



