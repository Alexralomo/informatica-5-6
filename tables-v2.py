def main():
    print("Hola soy Matematicas😨😨😨😨 y te preguntare las Tablas😱😱😱😱")
    print()
    while True:
        try:
            times_table = int(input("Elije un numero del 1 al 10, anda sin miedo😁😁😁😁 El numero que elijas es lo que te preguntare🫵 🫵 🫵 🫵: "))
            break
        except ValueError:
            print("pon un numero!😡😡😡😡😡😡😡😡😡😡😡😡")

    while True:

        try:
            tabla = int(input("Cuantas preguntas quieres que te diga?:"))
            break
        except ValueError:
            print("pon numero tu puedes no es complicado")



            if 1 <= times_table <= 10:
                print(f"mmm entonses quieres {tabla} preguntas")
                print()
                print(f"te are {tabla} preguntas de la tabla del {times_table}")

    while True:
        max_value = tabla
        for x in range(1,max_value + 1):

            answer = x * times_table
            try:
                user_answer = int(input(f"{x} se multiplica {times_table} is:"))
                break
            except ValueError:
                print("en numero porfa")



            if user_answer == answer:
                print("correcto vamos por la cigiente")

            elif user_answer != answer:
                print(f"no es correcto pero te explico, si {times_table} se multiplica por algo sumalo todas esas veses, la respuesta es {answer} intentalo con la cigiente")



if __name__ == "__main__":
    main()
