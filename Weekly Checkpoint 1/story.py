def main():
    # Goku = input("Goku:")

    # # Separation
    # print("hello!", Goku)

    # #Ending
    # print("hello", end=" ")
    # print(goku)

    # Concatenation
    # print("hello " + Goku)

    # #Formatted String
    # print(f"hello {Goku}")

    name= input("what is your name?").title().strip()
    color= input("Tell me a color:").lower().strip()
    adj=input("tell me an adjetive:")
    goal=input("A goal you would like to achieve:")
    print()
    print()
    print(f"hello {name}!")
    print()
    print()
    print()
    print("Esta es tu historia!!!!!!!!!!")
    print()
    print(f" Ase mucho tiempo estaba un chico llamado {name}, que le encantava el color {color}, y su mallor birtud es ser {adj}, y su metas es {goal}.")
    print()
    print()
    print(f" Ase mucho tiempo estaba un chico llamado {name}, que le encantava el color {color}, y su mallor birtud es ser {adj}, y su metas es {goal}.".upper())


if __name__== "__main__":
    main()
