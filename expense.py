import csv
import time
t = time.strftime("%H:%M:%S")
print(t)
from datetime import datetime


class Expense:
    def __init__(self, amount, category, date, description, quantity):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.quantity = quantity

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date.strftime('%Y-%m-%d'),
            'description': self.description,
            'quantity': self.quantity
     }
        
def save_expenses(expenses, filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date', 'description', 'quantity', 'total'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())

def load_expenses(filename='expenses.csv'):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense(
                    float(row['amount']),
                    row['category'],
                    datetime.strptime(row['date'], '%Y-%m-%d'),
                    row['description'],
                    int(row['quantity'])
                ))
        
    except FileNotFoundError:
        pass
    return expenses

def summarize_expenses(expenses):
    total_amount = 0
    total_quantity = 0
    for expense in expenses:
        total_amount += int(expense.amount)
        total_quantity += int(expense.quantity)

    return total_amount, total_quantity