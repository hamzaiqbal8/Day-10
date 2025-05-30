"""Add colors using ANSI codes (optional)"""

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"


while True:
    try:
        n = int(input(f"{CYAN}Enter the number of rows: {RESET}"))
        if n <= 0:
            print(f"{YELLOW} Please enter a number greater than 0.{RESET}")
        else:
            break
    except ValueError:
        print(f"{RED} Invalid input! Please enter a valid whole number.{RESET}")


for i in range(1, n + 1):
    print(GREEN + "* " * i + RESET)
