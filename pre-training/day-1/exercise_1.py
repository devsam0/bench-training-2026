# Data types and basic arithmetic
name = "Sam"
age = 26
drinks_coffee = True
monthly_salary = 120000.0  # float
print(f"Hi, I'm {name}. I am {age} years old. Coffee lover? {drinks_coffee}. Monthly earnings: Rs.{monthly_salary}")


# Calculations for years until retirement
RETIREMENT_AGE = 60
years_to_retirement = RETIREMENT_AGE - age
print(f"Retirement countdown: {years_to_retirement} years to go.")

# Calculations for the weekly coffee budget
coffee_price = 150
cups_per_day = 3
days_in_week = 7
weekly_coffee_budget = coffee_price * cups_per_day * days_in_week

print(f"Weekly caffeine tax: Rs.{weekly_coffee_budget}")