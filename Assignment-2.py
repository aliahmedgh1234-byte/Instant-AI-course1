team_members =int(input("number of team members"))
months = int(input("Number of months the project will take"))
monthly_salary =float(input("Monthly salary"))
cloud_cost =float(input("Total cloud cost for the whole project"))


salary_cost = team_members * months * monthly_salary
subtotal = salary_cost + cloud_cost
VAT = subtotal * 0.14
Total = subtotal + VAT


print(f"Salary cost: {salary_cost:,.2f}")
print(f"Subtotal: {subtotal:,.2f}")
print(f"VAT: {VAT:,.2f}")
print(f"Total: {Total:,.2f}")
