def main():

    not_validated = True
    while not_validated:


        try:
                number = int(input("Enter a number between 1 and 10:"))# SOLO SIRVE CON LOS NUMEROS ENTEROS
                    if number >=1 and number <=10:

                print("Number stord successfully.")#SI
            else:
                not_validated = False #----> break
        except ValueError:
                print("Enter a NUMBER.!😡😡😡😡😡😡😡😡😡😡😡😡")











if __name__ == "__main__":
    main()
