def main():
    # Read a file
    with open("sample.txt") as file:
        content= file.read()
        print(content)

    # Turn file into a list
    with open("sample.txt") as hoco_week:
        hoco_list = hoco_week.read().splitlines()

    for day in range(len(hoco_list)):
        print(f"Day {day+1}: {hoco_list[day]}")










if __name__ == "__main__":
    main()
