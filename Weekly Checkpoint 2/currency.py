def main():

    print("Vamos a ver si vamos a comer con los compas de otros paises")
    print()
    print()
    pesos = int(input("Cuanto ganaste en pesos mexicanos amigo?:"))
    soles = int(input("Cuanto ganaste en pesos soles amigo?:"))
    reais = int(input("Cuanto ganaste en pesos reais amigo?:"))

    soles1 = int(soles) *5.07
    print("De soles a pesos compa:", soles1)
    reais1 = int(reais) *3.28
    print("De reais a pesos compa:", reais1)

    print("todo omls en pesos")
    print()
    print()


    total = int(soles1) + int(reais1) + int(pesos)
    print("Juntaron:", total)
    usa = int(total) *17.06
    print("usa moneda:", usa)







if __name__== "__main__":
    main()
