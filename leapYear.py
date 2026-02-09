def is_leap_year(year):
    """
    Check if a year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4 AND
    - If divisible by 100, it must also be divisible by 400
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Example usage
if __name__ == '__main__':
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")