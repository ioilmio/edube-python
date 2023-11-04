# Your task is to write and test a function which takes two arguments (a year and a month)
# and returns the number of days for the given month/year pair (while only February is sensitive to the year value,
# your function should be universal).

# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful
# We encourage you to use a list filled with the months' lengths. You can create it inside the function
# - this trick will significantly shorten the code.

# We've prepared a testing code. Expand it to include more test cases.


def is_year_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


month31 = [1, 3, 5, 7, 8, 10]
month30 = [11, 4, 6, 9]


def check_month(month):
    if month == 2:
        return 28
    if month in month30:
        return 30
    if month in month31:
        return 31


def days_in_month(year, month):
    if month > 12 or month < 1:
        return None
    if year == 2000:
        return 29
    if is_year_leap(year) == True:
        return check_month(month)
    else:
        return check_month(month)


#
# Write your new code here.
#

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
