def main():

    print("What day is it today?")
    day = int(input())

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
