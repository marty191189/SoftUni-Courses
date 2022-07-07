hour_of_day = int(input())
day_of_week = input()

if 10 <= hour_of_day <= 18:
    if day_of_week == "Monday":
        print("open")
    elif day_of_week == "Tuesday":
        print("open")
    elif day_of_week == "Wednesday":
        print("open")
    elif day_of_week == "Thursday":
        print("open")
    elif day_of_week == "Friday":
        print("open")
    elif day_of_week == "Saturday":
        print("open")
    elif day_of_week == "Sunday":
        print("closed")

else:
    print("closed")
