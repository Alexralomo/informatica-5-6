import random

def main():

    coin = ["heads", "tails"]
    attempts = 10
    while attempts > 0:


        flip = random.choice(coin)
        guess = input("heads or teils?"). strip().lower()

        print("the coin landed on", flip)


        if guess == flip:
            print("you Won")
        else:
            print("you lost")
            attempts -= 1
            print("Attempts left:", attempts)









if __name__=="__main__":
    main()
