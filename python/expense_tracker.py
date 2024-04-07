class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})

    def total_expenses(self):
        return sum(item['amount'] for item in self.expenses)

    def list_expenses(self):
        for item in self.expenses:
            print(f"{item['description']}: ${item['amount']}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View List of Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(description, amount)
            print("Expense added successfully.")
        elif choice == '2':
            print(f"Total expenses: ${tracker.total_expenses()}")
        elif choice == '3':
            if tracker.expenses:
                print("List of Expenses:")
                tracker.list_expenses()
            else:
                print("No expenses recorded yet.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
