class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter number: "))
    if num < 0:
        raise NegativeNumberError
    print("Valid number")
except NegativeNumberError:
    print("Negative number not allowed")