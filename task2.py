expenses = []
total = 0

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    expense = float(input(f"Enter expense {i+1}: "))
    expenses.append(expense)
    total = total + expense

print("\nExpenses:", expenses)
print("Total Spent:", total)