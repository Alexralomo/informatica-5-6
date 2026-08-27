def main():

    #variables de la admosver
    eart_atmosfea = input("Quieres lansar una capsula al espacio dime a que capa lo lansas te pongo en cuanto tiempo llrga:")


    #Parte 1
    if eart_atmosfea == "troposphere":
        print("ufas se encuentra en el rango de 0–12 km")
    elif eart_atmosfea == "stratosphere":
        print("tu rango es de 12–50 km")
    elif eart_atmosfea == "mesosphere":
        print("tu rango es de 50–85 km")
    elif eart_atmosfea == "hermosphere":
        print("rango 85–700 km")
    elif eart_atmosfea == "exosphere":
        print("rango 700–10,000 km")
    else:
        print(" lo mas seguro es que lo escribiste mal son estas:___troposphere____stratosphere___mesosphere___hermosphere___exosphere, puedes escirbir una de esas porfa")

    # parte 2
    tiempo = int(input("hora dime en que kilometro quieres soltarlo:"))

    if tiempo < 12:
        print("este es el tiempo es en segundos:", tiempo*1000/20)
    elif tiempo < 50:
        print("este es el tiempo es en segundos: ", tiempo*1000/20 + tiempo*1000/75)
    elif tiempo < 85:
        print ("tiempo en segundos", tiempo*1000/20 + tiempo*1000/75 + tiempo*1000/200)
    elif tiempo < 700:
        print ("tiempo en segundos", tiempo*1000/20 + tiempo*1000/75 + tiempo*1000/200 + tiempo*1000/500)
    elif tiempo < 10000:
        print ("tiempo en segundos", tiempo*1000/20 + tiempo*1000/75 + tiempo*1000/200 + tiempo*1000/500 + tiempo*1000/2000)


if __name__== "__main__":
    main()
