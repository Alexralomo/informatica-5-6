import random
def main():

    largest("lista.txt")
def largest(letras):
    print("vamos a jugar a un orcado y seleciona las palabras solo te diremos el numero de letras que tiene")
    with open(letras) as palabra:
        selexiona= palabra.read().splitlines()
        selexion = random.choice(selexiona)

        for i in range(len(selexion)):
            print(i+1)
        input("pon tu letra:")
        



















if __name__=="__main__":
    main()
