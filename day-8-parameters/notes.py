def prime_checker(number):
    if number == 0 or number == 1:
        return print("It's not a prime number.")
    
    for num in range(2, number):
        if number % num == 0:
            return print("It's not a prime number.")
    print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(n)
# OR
# prime_checker(number=n)
