"""Hello Every one"""

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    spaces = n - i
    for s in range(spaces):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
