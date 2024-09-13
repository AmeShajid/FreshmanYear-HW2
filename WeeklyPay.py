

# known facts: hourlyrate = 7.25
"""
1. get the hours worked in a week
2. validate hours worked, hours should be between 0 and 60
3. if works worked are up to 40
    a. weekly pay = hours worked * hourly rate
    else the person worked more than 40 hours
        a. first 40 hours at the regular rate: hoursworked * hourlyrate
        b. calculate overtime: (hoursworked - 40) * 1.5 * hourlyrate
        c. pay = first40hours + overtime
4. display results
5. if bad hours, display error
"""

#known facts
hourly_rate = 15.50

#get input from user about hours worked and then validate
hoursworked = int(input("How many hours did you work"))

if hoursworked >= 0 and hoursworked <= 60:#this means its good data
    #check if hours is up to 40 hours
    if hoursworked <= 40:
        weekly = hoursworked * hourly_rate
    else: #means employee worked more than 40 hrs
        first40hours = 40 * hourly_rate
        overtime = (hoursworked - 40) * 1.5 * hourly_rate
        weeklypay = first40hours + overtime

    print("You worked", hoursworked, "hours this week")
    print("Your weekly pay is", weeklypay)
else:
    print("Too many hours")