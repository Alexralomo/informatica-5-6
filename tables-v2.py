def main():
    while True:
        try:

            print("Hola soy Matematicas😨😨😨😨 y te preguntare las Tablas😱😱😱😱")
            print()
            times_table = int(input("Elije un numero del 1 al 10, anda sin miedo😁😁😁😁 El numero que elijas es lo que te preguntare🫵 🫵 🫵 🫵: "))
        except ValueError:
                    print("pon un numero!😡😡😡😡😡😡😡😡😡😡😡😡")


        while True:

                            tabla = int(input("Cuantas preguntas quieres que te diga?:"))
                            if 1 <= times_table <= 10:
                                print(f"mmm entonses quieres {tabla} preguntas")

                                print(f"Here is the {times_table} times table")

                                for x in range(1, 11):
                                    answer = x * times_table
                                    print(f"{x} times {times_table} is {answer}")
                            else:
                                print("Invalid command.")


if __name__ == "__main__":
    main()
