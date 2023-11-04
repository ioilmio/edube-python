def day_of_year(year, month, day):
    # Check for valid inputs
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        return None

    if month < 1 or month > 12 or day < 1:
        return None

    # Define days in each month
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29

    # Check if the provided day is valid for the given month
    if day > days_in_month[month]:
        return None

    # Calculate the day of the year
    day_of_year = sum(days_in_month[:month]) + day

    return day_of_year

# Testing the function
year = 2023
month = 11
day = 4
result = day_of_year(year, month, day)
print(f"Day of the year: {result}")
