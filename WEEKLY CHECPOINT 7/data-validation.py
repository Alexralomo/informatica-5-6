def main():

    not_validated = True
    while not_validated:


        try:
                number = int(input("Enter a number between 1 and 10:"))# SOLO SIRVE CON LOS NUMEROS ENTEROS
                if number >= 1 and number >=10:
                    print("Number stord successfully.")#SI
                    not_validated = False #----> break
                else:
                    print("That number is not between 1 and 10. try again.")
        except ValueError:
                print("Enter a NUMBER.!😡😡😡😡😡😡😡😡😡😡😡😡")

    while True:
        try:
            name = input("Enter your name:")
            f_letter= name[0]
            print("Name stored successfully.")
            break
        except IndexError:
            print("A name is required.")









if __name__ == "__main__":
    main()
