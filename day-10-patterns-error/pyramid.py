"""pyramid.py"""

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1, 1):
    stars = 2 * i - 1
    spaces = n - i
    print(" " * spaces + "*" * stars + " " * spaces)
