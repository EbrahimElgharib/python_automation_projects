# 6- Birthday Calculator
# 7- Age Calculator

  
from datetime import date
'''
# Get a date from User
day = int(input("Enter an int Day : "))
month = int(input("Enter an int month : "))
year = int(input("Enter an int year : "))
my_birthday = date(year,month,day)
'''

'''
# get date from user with split
date_list = input("Enter date with format yyyy-mm-dd : ").split('-')
year, month, day = [int(item) for item in date_list]
my_birthday = date(year, month, day)
'''


# Age Calculator
# let
my_birthday = date(1997,4,7)
today = date.today()

months = today.month-my_birthday.month
days = today.day-my_birthday.day

n_days = months*30 + days
print(f"Number of Days until Birthday = {n_days} days")

# Age Calculator
age_days = today - my_birthday
age_year = age_days.days//365
print(f"Your Age = {age_year} years")
