def main():

    year = int(input("pon los años que quieres adelantar:"))
    transistors = 17.8


    current_year = 2026

    if (current_year + year) >=2030:
    print("the law is not valid.")
    else:
        transistors *= 2** (year/2)
        print("transistors:",transistors)




if __name__== "__main__":
    main()

