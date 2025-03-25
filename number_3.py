def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_extended(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return gcd(numbers[0], gcd_extended(numbers[1:]))


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_extended(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return lcm(numbers[0], lcm_extended(numbers[1:]))


def UserInput():
    number_count = int(input("Enter the number of numbers: "))
    numbers = []
    for i in range(number_count):
        number = int(input(f"Enter number {i+1}: "))
        numbers.append(number)

    result = lcm_extended(numbers)
    print(f"The lcm of {numbers} is {result}")


# UserInput()
