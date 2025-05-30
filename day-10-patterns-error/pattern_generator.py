"""pattern_generator.py"""

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

def print_square(n, symbol):
    """pattern_generator.py"""
    for _ in range(n):
        print(symbol * n)

def print_triangle(n, symbol):
    """pattern_generator.py"""
    for i in range(1, n + 1):
        print(symbol * i)

def print_reverse_triangle(n, symbol):
    """pattern_generator.py"""
    for i in range(n, 0, -1):
        print(symbol * i)

def print_pyramid(n, symbol):
    """pattern_generator.py"""
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + symbol * stars)

def get_valid_rows():
    """pattern_generator.py"""
    while True:
        try:
            n = int(input(f"{CYAN}Enter number of rows: {RESET}"))
            if n <= 0:
                print(f"{YELLOW}Please enter a positive number.{RESET}")
                continue
            return n
        except ValueError:
            print(f"{RED}Invalid input! Please enter a number.{RESET}")

def get_valid_pattern():
    """pattern_generator.py"""
    valid_patterns = ["square", "triangle", "reverse", "pyramid"]
    while True:
        pattern = input(f"{CYAN}Choose a pattern (square, triangle, reverse, pyramid): {RESET}").lower()
        if pattern in valid_patterns:
            return pattern
        print(f"{RED}Invalid pattern type. Please choose from square, triangle, reverse, pyramid.{RESET}")

def main():
    """pattern_generator.py"""
    while True:
        print(f"{GREEN}\n--- Pattern Generator ---{RESET}")
        
        pattern = get_valid_pattern()
        rows = get_valid_rows()
        symbol = input(f"{CYAN}Enter symbol to print: {RESET}")

        print(f"\n{YELLOW}Generated Pattern:{RESET}\n")

        if pattern == "square":
            print_square(rows, symbol)
        elif pattern == "triangle":
            print_triangle(rows, symbol)
        elif pattern == "reverse":
            print_reverse_triangle(rows, symbol)
        elif pattern == "pyramid":
            print_pyramid(rows, symbol)

        again = input(f"\n{CYAN}Do you want to build another pattern? (yes/no): {RESET}").lower()
        if again != "yes":
            print(f"{GREEN}Thank you for using Pattern Generator. Goodbye!{RESET}")
            break

if __name__ == "__main__":
    main()
