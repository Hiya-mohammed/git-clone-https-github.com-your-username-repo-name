def display_right_angle_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        print('1 ' * i)

def display_palindromic_triangle():
    n = int(input("Enter the number of rows: "))
    for i in range(1, n + 1):
        print(' '.join(str(j) for j in range(1, i + 1)) + ' ' + ' '.join(str(j) for j in range(i - 1, 0, -1)))

def display_help():
    print("This program displays a right-angle triangle of ones or a palindromic triangle.")
    print("Option 1: Display a right-angle triangle of ones.")
    print("Option 2: Display a palindromic triangle.")
    print("Option 3: Display this help message.")
    print("Option 4: Exit the program.")

def main():
    while True:
        print("\nMenu:")
        print("1. Display a right-angle triangle of ones")
        print("2. Display a Palindromic Triangle")
        print("3. Help")
        print("4. Exit")
        option = input("Enter your choice: ")
        if option == '1':
            display_right_angle_triangle()
        elif option == '2':
            display_palindromic_triangle()
        elif option == '3':
            display_help()
        elif option == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
