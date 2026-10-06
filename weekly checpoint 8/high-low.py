def main():
    def Altura(a, b):
        if a < b:
            highest_num = b
        else:
            highest_num = a

        print(f"El numero mas grande es {highest_num}" )
    Altura(2,8)




    def menor(a,b,c):
        if a < b and c:
            menor_l = a
        elif b < a and c:
            menor_l = b
        else:
            menor_1 = c
    print(f"el numero menor es {menor}")
    menor(2,3,4)

    num_1 = int(input("Pon un numero entero porfa:"))
    num_2 = int(input("Pon un numero entero porfa:"))
    num_3 = int(input("Pon un numero entero porfa:"))

    menor(num_1, num_2, num_3)



























if __name__ == "__main__":
    main()
