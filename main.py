# Expense tracker
#Mini Project - Expense Tracker
'''Question / Problem Statement: Create a console-based Expense Tracker program
in Python that allows the user to record daily expenses and view summaries 
like total spending. Use only the concepts learned 
(loops, conditionals, lists, dictionaries, and basic input/output).'''
#-------------------------------------------------------------------
#Project Details / Description:
'''You are required to build a simple personal finance management tool.
The program should allow the user to:
Add an expense with details like date, category, description, and amount.
View all recorded expenses in a clean format.
Calculate total spending so far.
Exit the program gracefully when the user chooses to.'''
#without using user defined functions and file handling
#-------------------------------------------------------------------
# List to hold all expenses as dictionaries with keys: date, category, description, amount
expensesList = []

print("\nWelcome to Expense Tracker:💸")

while True:
    # Main menu
    print('=======MENU=======')
    print('1.Add Expenses')
    print('2.View All Expenses')
    print('3.View Total Spending')
    print('4.Exit')

    # Read user choice
    try:  # Try to convert user input to integer
        choice = int(input('Enter your choice:'))  # Get user input and convert to integer
    except ValueError:  # Catch error if input cannot be converted to integer
        print('Invalid input. Please enter a number.')  # Display error message
        continue  # Skip to next iteration of loop

    # Add a new expense
    if choice == 1:
        print("\n--- Add New Expense ---")
        date = input('Enter the date:')  # e.g., 12jun
        category = input('Enter the category(e.g.,food,travel,shopping....):')
        description = input('Enter short details:(e.g.,burger,trip...):')
        amount = float(input('Enter the amount:'))  # convert to float for calculations

        expense = {'date': date, 'category': category, 'description': description, 'amount': amount}
        expensesList.append(expense)
        print('\n---------DONE.....Expenses added succesfully--------')

    # View all recorded expenses
    elif choice == 2:
        if len(expensesList) == 0:
            print("---No expenses added---\'Money saved\'")
        else:
            print('====Your expense====')
            count = 1
            for eachExpense in expensesList:
                # Print each expense in a readable format
                print(f"Expense{count}->{eachExpense['date']},{eachExpense['category']},{eachExpense['description']},{eachExpense['amount']}")
                count += 1

    # Calculate and display total spending
    elif choice == 3:
        total = 0
        for eachexpense in expensesList:
            total = total + eachexpense['amount']

        print('\nYour Total Spending:', total)

      # Exit the program
    elif choice == 4:
        print('\nThank you for using Expense Tracker. Goodbye!🙏')
        break

    else:
        # Invalid menu choice
        print('Invalid Choice.Try again...........')

# Example output (for reference)
'''
Welcome to Expense Tracker:💸
=======MENU=======
1.Add Expenses
2.View All Expenses
3.View Total Spending
4.Exit
'''