# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
     # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    initial_balance = float(input("Enter the initial savings account balance (e.g., 1000): "))
    #soliciting the intial balance
    annual_interest_rate = float(input("Enter the annual savings interest rate (in percentage, e.g., 5): "))
    #soliciting annual interest rate
    duration_months = int(input("Enter the duration in months (e.g., 12): "))
    #soliciting total months duration


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(initial_balance, annual_interest_rate, duration_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    #make sure to format this to 2 decimal places
    print (updated_savings_balance)
    print (interest_earned)
    
    #reread instructions for formatting the above ^

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    ##try:[for here - make it a for loop instead of current structure so that can message the user to make sure to enter a number w/o breaking the code
    initial_cd_balance = float(input("Enter the initial cd account balance (e.g., 1000): "))
    #soliciting the intial balance
    annual_cd_interest_rate = float(input("Enter the annual cd interest rate (in percentage, e.g., 5): "))
    #soliciting annual interest rate
    duration_cd_months = int(input("Enter the duration in months (e.g., 12): "))
    #soliciting total months duration
    ## except ValueError:
       ## print("Invalid input! Please enter a number for each: balance, interest rate, and duration.")
 

#for loop instead of this ^ so that customer can go back to beginning of 'try' to put the right value in
    updated_cd_balance, cd_interest_earned = create_cd_account(initial_cd_balance, annual_cd_interest_rate, duration_cd_months)
#add messages for all the print displays
    print (updated_cd_balance)
    print (cd_interest_earned)

if __name__ == "__main__":
    # Call the main function.
    main()