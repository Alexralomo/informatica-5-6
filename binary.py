def main():
    print("hola bamos a combertir tu numero binarios a numeros normales estas listo")
    print()

    valid_bits = ["0", "1"]
    while True:
        correct_chars = 0
        binary_number = input("enter your binary number:")
        for i in binary_number:
            if i in valid_bits:
                correct_chars += 1


        binary_to_decimal(binary_number)

def binary_to_decimal(binary):

    decimal = 0
    for bit in binary:
        decumal = (decimal * 2) + int(bit)
    print(decumal)







if __name__ == "__main__":
    main()
