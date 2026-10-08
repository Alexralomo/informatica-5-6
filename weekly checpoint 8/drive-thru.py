def main():
    welcome()
    ordenes = int(input("dime el numero de lo que pediste:"))
    get_item(ordenes)
def welcome ():
    menu = ["tacos", "pollo", "quesadilla" , "papitas", "pastel", "perros para adoptar"]
    print("Hola bienbenido a mi localcito de comida rapida, tenemos este este es nuestro menu")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")



def get_item (orden):
    if orden == 1:
        print("🌮")
    elif orden == 2:
        print("🍗")
    elif orden == 3:
        print("🌮 + 🧀")
    elif orden == 4:
        print("🍟")
    elif orden == 5:
        print("🎂")
    elif orden == 6:
        print("🐕‍🦺")





if __name__ == "__main__":
    main()
