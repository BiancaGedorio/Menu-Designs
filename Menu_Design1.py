def get_menu_choice():
    global choice

    def print_menu():       # Menu Design
        print(30 * "-", "MENU", 30 * "-")
        print("1. ")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            print(1)
        elif choice == '2':
            while len(choice) == 0:
                print(2)
        elif choice == '3':
            while len(choice) == 0:
                print(3)
        elif choice == '4':
            while len(choice) == 0:
                print(4)
        elif choice == '5':
            int_choice = -1
            loop = False
        else:
            # Any inputs other than values 1-4 will print an error message
            input("")
    return [int_choice, choice]


get_menu_choice()
