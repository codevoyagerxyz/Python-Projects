expenses = []
n = int(input("How many expenses do you want to enter? "))
for i in range(n):
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
total = sum(expenses)
maximum = max(expenses)
print("\n--- Expense Summary ---")
print("Total Expenses:", total)
print("Highest Expense:", maximum)
