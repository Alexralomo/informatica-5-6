import random
def main():

    largest("lista.txt")
def largest(letras):
    with open(letras) as palabra:
        selexiona= palabra.read().splitlines()
        selexion = random.choice(selexiona)

        














if __name__=="__main__":
    main()
