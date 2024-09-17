import locale
from datetime import datetime

# Set the locale to French
locale.setlocale(locale.LC_TIME, 'fr_FR')

current_date = datetime.now().date()

minute = datetime.now().minute
hour = datetime.now().hour
day = current_date.strftime("%d")
month = current_date.strftime("%B")
year = current_date.strftime("%Y")

print(f'minute = {minute}')
print(f'hour = {hour}')
print(f'day = {day}')
print(f'month = {month}')
print(f'year = {year}')