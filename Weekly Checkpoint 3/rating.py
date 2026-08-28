def main():

    restaurante = int(input("Estrellas del restaurante 1-5:"))


    if restaurante < 1:
        print("No me gusta")
    elif restaurante < 2:
        print("Ups perdon por el serbicio")
    elif restaurante < 3:
        print("bueno bueno te gusto la comidda")
    elif restaurante < 4:
        print("te esperamos pronto")
    elif restaurante < 5:
        print("tienes un descuento")
    else:
        print("Es de 1-5 compa")






if __name__== "__main__":
    main()
