from datetime import datetime
def main():

    day = datetime.now().weekday()
    days = ["Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "sunday"]
    print(days[day])
    print(day)
    months = ["January", "February", "March", "Abril", "May", "June", "July", "August", "September", "October", "November", "December"]
    print("These are the summer months:")
    print(months[5])
    print(months[6])
    print(months[7])


    print("What day is it today?")



    if day < 4:
        print("It's a weekday")
        remaing = 5 - day
        print(remaing, "day until the weekend")
    elif day == 4:
        print("it's Friday")
        print("just a day left until the weekend")
    else:
        print("It's the weekend!!!")





if __name__=="__main__":
    main()
