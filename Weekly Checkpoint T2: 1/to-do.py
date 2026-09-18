def main():

    print("hola bienbenidos a tacoas 2 hermanos")
    print()
    print()
    print("Este es su task comensemos entonses a crearla")

    list = []
    while True:
        print(f"Tasks to do: {len(list)}")
        print(list)

        usario_list = input("ENTER YOU LIST").Capitalize().strip()
        if usario_list == "Exit":
            break
        if usario_list not in tasks:
            tasks:append(usario_list)
        elif usario_list in task:
            del_confirm = input(f"Did you complet {nuw_task}?(Y/N):").lower().strip()
            if del_confirm =="Y":
                tasks.remove(new_task)
            else:
                continue

























if __name__ == "__main__":
    main()
