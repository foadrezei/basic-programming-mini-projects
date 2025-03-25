# this func checks if a number is prime or not
def isPrime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            # number is non-prime
            return False
    return True

# this func do the factorizasion process


def factorize(number):
    primeFactors = []
    divisor = 2
    if isPrime(divisor):  # check if our divisor is prime
        while number > 1:
            if number % divisor == 0:
                primeFactors.append(divisor)
                number //= divisor
            else:
                divisor += 1  # checking prime factors in order
    else:
        divisor += 1  # try to make a prime divisor
    return primeFactors

import main
# User Input section
def UserInput():
    print('Eg: 20 = 2^2 * 5 here the input is 20')
    number = int(input("Enter a number you want to be factorised: "))

    result = factorize(number)

    # Display the prime factorization
    output = str(number) + " = "
    factors = []
    for factor in result:
        count = result.count(factor)
        if factor not in factors:
            if count > 1:
                factors.append(factor)
                output += str(factor) + "^" + str(count) + " * "
            else:
                factors.append(factor)
                output += str(factor) + " * "
    output = output.rstrip(" * ")
    print(output)
    

# UserInput()
