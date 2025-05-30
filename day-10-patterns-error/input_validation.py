"""input_validation.py"""


while True:
    try:
        n = int(input("Enter the number of rows: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

for i in range(1, n + 1):
    print("*" * i)
