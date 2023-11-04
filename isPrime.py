def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check if the number is divisible by 2 or 3
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Start checking for prime factors from 5 onwards
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

# Testing the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")





# def is_prime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True

#     if num % 2 == 0:
#         return False

#     # Check divisibility by odd numbers from 3 to the square root of the number
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False

#     return True

# # Testing the function
# num = 17
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
