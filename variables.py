hourly_rate = 300.0
overtime_rate = 1.5
overtime = hourly_rate * overtime_rate
standard_hours = 40
hours_worked = 60

def workTimeAndIncome(hours_worked,overtime,standard_hours,hourly_rate):
    income = ((hours_worked - standard_hours)*overtime) + (standard_hours *hourly_rate)
    print("This week I worked")
    print(str(hours_worked) + " hour(s)")
    print("I made")
    print(str(income) + "$ in total")
    print("This week")

workTimeAndIncome(hours_worked,overtime,standard_hours,hourly_rate)

