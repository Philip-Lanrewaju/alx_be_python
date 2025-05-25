# These lines of code calculates users monthly savings

# This requests and record users monthly income
MonthlyIncome = float(input("Enter your monthly income:"))


# This requests and record the users monthly expense
MonthlyExpense = float(input("Enter your total monthly expense:"))


# This calculates Users Monthly savings
MonthlySavings = MonthlyIncome - MonthlyExpense


# This prints users monthly savings
print(f"Your monthly savings are ${MonthlySavings}.")


# This calculates users Projected savings after one year
ProjectedSavings = MonthlySavings*(12 + (MonthlySavings * 12 * 0.05))


# This prints the projected savings after one year.
print(f"Projected savings after one year, with interest, is: ${ProjectedSavings}.")
