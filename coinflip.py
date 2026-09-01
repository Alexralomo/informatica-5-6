import random

def main():

    usario = int(input("elije agila sello:"))


    moneda = random.randint (1, 2)
    print(moneda)

    if moneda ==1:
        print("sello")
    elif moneda == 2:
        print("agila")











if __name__=="__main__":
    main()
