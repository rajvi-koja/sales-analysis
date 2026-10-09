# Project 1: Simple Expense Tracker

# A list of dictionaries keeping track of our expenses
expenses = [
    {"category": "Food", "amount": 15.50},
    {"category": "Transport", "amount": 7.00},
    {"category": "Food", "amount": 12.30},
    {"category": "Entertainment", "amount": 25.00}
]

print("--- EXPENSE REPORT ---")

# Calculate total expenses
total_expenses = 0
for item in expenses:
    total_expenses += item["amount"]

print(f"Total overall expenses: {total_expenses} €")

# Find the highest expense
highest_expense = max(expenses, key=lambda x: x["amount"])
print(f"Highest expense was for: {highest_expense['category']} with {highest_expense['amount']} €")