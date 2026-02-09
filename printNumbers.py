def print_numbers(n):
    """
    Print numbers from 1 to n as a single string.
    n must be between 1 and 150 (inclusive).
    """
    if 1 <= n <= 150:
        print(''.join(str(i) for i in range(1, n + 1)))
    else:
        print("n must be between 1 and 150")


# Example usage
if __name__ == '__main__':
    n = int(input())
    print_numbers(n)