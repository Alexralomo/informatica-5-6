def main():

    answer = ""
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").strip().title()
        if answer == "Yes":
            followup = imput("Really?").strip().title()
        if followup == "Yes!":
            break

    print("we just arrived!")


if __name__=="__main__":
    main()

