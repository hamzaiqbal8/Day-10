"""pattern_validator.py"""

try:
    n = int(input("Enter the number of rows: "))

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

except ValueError:
    print("Please enter a valid number (only digits allowed).")
