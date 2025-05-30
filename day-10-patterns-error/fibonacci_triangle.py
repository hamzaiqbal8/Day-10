"""fibonacci_triangle.py"""

n = int(input("Enter the number of rows: "))

a, b = 0, 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(a, end=" ")
        a, b = b, a + b
    print()
