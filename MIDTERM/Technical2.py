import datetime

date_input = input("Enter the date (mm/dd/yyyy): ")

try:
    date_obj = datetime.datetime.strptime(date_input, "%m/%d/%Y")
    formatted_date = date_obj.strftime("%B %d, %Y")
    print("Date Output:", formatted_date)
except ValueError:
    print("Invalid date format. Please use mm/dd/yyyy.")
