def main():

    answer = ""
    followup = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").strip()
        if answer == "Yes":
            followup = input("Really?").strip()
        if followup == "Yes!":
            break

    print("we just arrived!")


if __name__=="__main__":
    main()

