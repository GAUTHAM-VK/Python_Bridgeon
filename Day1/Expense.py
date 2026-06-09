total=0
expenses= []
for i in range(1,8):
    expense=float(input(f"enter the expense in day {i}: "))
    expenses.append(expense)
total=sum(expenses)
average=total/7
print("Total Expense: ", total)
print("Average Expense: ", average)
highest=max(expenses)
lowest=min(expenses)
print("Highest Expense: ", highest)
print("Lowest Expense: ", lowest)