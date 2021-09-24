"""A simple python script to calculate Age
Author: Mohamed"""

import datetime

year_born = int(input("What year were you born? "))
now = datetime.datetime.now()
age = now.year - year_born



#print(now.year, now.month, now.day, now.hour, now.minute, now.second)
print(f"You are {age} years old.")
