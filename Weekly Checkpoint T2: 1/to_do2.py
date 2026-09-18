def main():

    tasks = []
    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)

        nuw_task = input("Enter task: ").capitalize().strip()
        if nuw_task =="Exit":
            break

        if nuw_task not in tasks:
            tasks.append(nuw_task)
        elif nuw_task in task:
            del_confirm = input(f"Did you complet {nuw_task}?(Y/N):").lower().strip()
            if del_confirm =="Y":
                tasks.remove(new_task)
            else:
                continue




if __name__ == "__main__":
    main()
