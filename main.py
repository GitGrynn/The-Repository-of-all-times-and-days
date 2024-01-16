expenses = []

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    for counter, expense in enumerate(expenses, 1):
        print(f"{counter}. Amount: {expense['amount']}, Category: {expense['category']}")

def removeExpense():
    while True:
        listExpenses()
        print("Enter the number of the expense you want to remove (0 to cancel):")
        try:
            expenseToRemove = int(input(">"))
            if 0 < expenseToRemove <= len(expenses):
                del expenses[expenseToRemove - 1]
                print("Expense removed successfully.")
                break
            elif expenseToRemove == 0:
                print("Operation canceled.")
                break
            else:
                print("Invalid input. Please enter a valid expense number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)
    print("Expense added successfully.")

def printMenu():
    print("Please choose from the following options...")
    print("1. Add a new expense")
    print("2. Remove an expense")
    print("3. List all expenses")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == '1':
            print("Enter the amount for the new expense:")
            while True:
                try:
                    amountToAdd = float(input("> "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            print("Enter the category for the new expense:")
            category = input("> ")

            addExpense(amountToAdd, category)

        elif optionSelected == '2':
            removeExpense()

        elif optionSelected == '3':
            listExpenses()

        elif optionSelected == '0':
            print("Exiting the expense management system. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")