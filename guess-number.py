import random
def main():

    lasar = random.randint(1,100)



    name= input("what is your name?:").title().strip()
    peligro = input("pon tu dificultad amigo, Facil😁😁😁, Medio👾👾👾👾, demonio ultra dificil😈😈😈😈:").title().strip()
    if peligro == "Facil":
        print(f"Well, {name}, I am thinking of a number between 1 and 100 Take a guess:")
    print()
    print()
    numeros = int(input("que numero piensas que es:"))

    while numeros != lasar:

        if numeros > lasar:
            print("loco, el numero es muy alto🪜🪜🪜🪜🪜")
        elif numeros < lasar:
            print("loco, el numero es muy abajo🦴🦴🦴🦴")

        numeros = int(input("elije otravez👀👀👀:" ))

        if numeros == lasar:
            print(" lo lograste loco🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")

















if __name__=="__main__":
    main()
