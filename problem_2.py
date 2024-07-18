def decimal_to_binary(n):
    binary = []
    while n > 0:
        remainder = n % 2
        binary.append(str(remainder))
        n = n // 2
    return ''.join(reversed(binary))

decimal_number = int(input("Enter a positive decimal number: "))
while decimal_number <= 0:
    print("Please enter a positive decimal number.")
    decimal_number = int(input("Enter a positive decimal number: "))

binary_number = decimal_to_binary(decimal_number)
print("The binary equivalent of", decimal_number, "is", binary_number)
