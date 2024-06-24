from expense import Expense, save_expenses, load_expenses,summarize_expenses
from datetime import datetime

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    quantity = input("Enter quantity: ")
    expense = Expense(amount, category, datetime.strptime(date, '%Y-%m-%d'), description, quantity)
    expenses.append(expense)

def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense.date} - {expense.category}: ${expense.amount} ({expense.description}){expense.quantity}")

def main():
    expenses = load_expenses()
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Save and exit")
        print(f"Total expenses: ${summarize_expenses(expenses)}")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
        elif choice == '4':
            summarize_expenses(expenses)
            break

if __name__ == "__main__":
    main()