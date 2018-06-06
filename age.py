import datetime

date_entry = input('Enter a date in YYYY-MM-DD format')
year: object
year, month, day = map(int, date_entry.split('-'))
today = datetime.date.today()
age = today.year-year
print("You are" + str(age) + "years.old")
