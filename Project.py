def main():
    """Main function to run the Budget Tracker."""
    print("Welcome to the Budget Tracker!")
    expenses = []
    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total expenses: ${total:.2f}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def add_expense(expenses):
    """Add an expense to the list."""
    try:
        item = input("Enter the item name: ")
        cost = float(input(f"Enter the cost of {item}: $"))
        expenses.append({"item": item, "cost": cost})
        print(f"Added {item} for ${cost:.2f}.")
    except ValueError:
        print("Invalid input. Please enter a valid cost.")

def view_expenses(expenses):
    """View all recorded expenses."""
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['item']} - ${expense['cost']:.2f}")

def calculate_total(expenses):
    """Calculate the total of all expenses."""
    return sum(expense["cost"] for expense in expenses)

if __name__ == "__main__":
    main()
