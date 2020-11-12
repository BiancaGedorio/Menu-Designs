# Menu and SubMenu Design

# Displaying the Main Menu
def main_menu():
    print("\n\t Welcome to the Main Menu")
    menu = "\n\t1: " \
           "\n\t2: " \
           "\n\t3: " \
           "\n--> "
    # The menu loop and user input of option
    while True:
        try:
            number = int(input(menu))
            if number == 1:
                sub_menu()
                break
            elif number == 2:
                print("")
                break
            elif number == 3:
                break
            else:
                print("Invalid. Enter 1-3. Try Again.")
        except ValueError:
            print("Error")
    return number


def sub_menu():
    print("\n\tSub Menu")
    submenu = "\n\tInstructions" \
              "\n\t1: " \
              "\n\t2: " \
              "\n\t3: " \
              "\n\t4: " \
              "\n--> "
    # The menu loop and user input of option
    while True:
        try:
            submenu_number = int(input(submenu))
            if submenu_number == 1:
                print("")
            elif submenu_number == 2:
                print("")
            elif submenu_number == 3:
                break
            else:
                print("Invalid. Enter 1-3. Try Again.")
        except ValueError:
            print("Error")
    return submenu_number


main_menu()
