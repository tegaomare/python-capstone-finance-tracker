# Author: Tega Omarejedje
# Project: Personal Finance Tracker
# Date: 06/21/2025

def print_welcome():
    print("Welcome to the Personal Finance Tracker!")

def add_expense(data):
    """Add an expense to the tracker."""
    try:
        description = input("Enter expense description: ").strip()
        if not description:
            raise ValueError("Description cannot be empty.")

        category = input("Enter category: ").strip()
        if not category:
            raise ValueError("Category cannot be empty.")

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)
        if amount < 0:
            raise ValueError("Amount must be positive.")

        # Store as (description, amount)
        if category not in data:
            data[category] = []
        data[category].append((description, amount))

        print("Expense added successfully.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def view_expenses(data):
    """Print all expenses by category."""
    if not data:
        print("No expenses recorded.")
        return
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for description, amount in expenses:
            print(f"  - {description}: ${amount:.2f}")

def view_summary(data):
    """Print total amount spent per category."""
    if not data:
        print("No expenses recorded.")
        return
    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def show_menu():
    """Display the menu options."""
    print("\nWhat would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

def main():
    print_welcome()
    data = {}  # Dictionary to store categorized expenses

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            view_summary(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
