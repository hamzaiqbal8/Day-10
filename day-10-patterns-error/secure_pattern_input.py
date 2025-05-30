"""secure_pattern_input.py"""

while True:
    try:
        n = int(input("Enter the number of rows: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")
