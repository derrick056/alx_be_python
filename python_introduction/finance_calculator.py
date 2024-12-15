#assingning of valiables

monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))
annual_interest_rate = 0.05
monthly_savings = monthly_income - total_monthly_expenses

Projected_savings = monthly_savings * 12 + ( monthly_savings * 12 * 0.05)

print ( "Projected savings after one year, with interest, is: $", Projected_savings ,".")