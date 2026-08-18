def main():

    goku = 5






    width = int(input("Enter the width of rectangle:"))
    print("0" * width)
    print("0" * width)
    print("0" * width)
    print("0" * width)
    print("0" * width)

    vegeta = int(goku) + int (goku) + int (width) + int (width)
    print("Perimetro:",vegeta)
    vegeto = int(goku) * int(width)
    print("Area:" , vegeto)
    pelon = (int(goku)**2 + int(width)**2)**1/2
    print("diagonal:" , pelon)


if __name__== "__main__":
    main()
