def main():

    largest("numbers.txt")
def largest(file):
    with open(file) as num_file:
        num_list= num_file.read().splitlines()
    print(num_list)

    #for i in range(len(num_list)):
       # num_list = int(num_list[i])
   # print(max(num_list))
if __name__ == "__main__":
    main()

