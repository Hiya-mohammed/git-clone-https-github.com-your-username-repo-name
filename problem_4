def process_list():
    # Get the list of integers from the user
    num_list = input("Enter a list of integers (separated by space): ")
    num_list = [int(x) for x in num_list.split()]

    # Create a new list of squares of even numbers
    even_squares = [x**2 for x in num_list if x % 2 == 0]
    print("List of squares of even numbers:", even_squares)

    # Get the start and end indices from the user
    start_index = int(input("Enter the start index: "))
    end_index = int(input("Enter the end index: "))

    # Slice the original list to extract a sublist
    sublist = num_list[start_index:end_index]
    print("Sublist from index", start_index, "to", end_index, ":", sublist)

if __name__ == "__main__":
    process_list()
