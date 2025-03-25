def approximate_integral(f, a, b, n):
    # f is the the function we want to calculate the definite integral
    # a is lover limit
    # b is upper limit
    # n is the number of sub-intervals
    h = (b - a) / n  # Calculate the width of each subinterval
    integral_sum = 0

    for i in range(n):
        x0 = a + i * h  # Calculate the left endpoint of the subinterval
        x1 = a + (i + 1) * h  # Calculate the right endpoint of the subinterval
        # Approximate the integral using the trapezoidal rule
        integral_sum += h * (f(x0) + f(x1)) / 2

    return integral_sum


def factorial(n):
    # base case
    if n <= 1:
        return n

    else:
        # recursion
        return n*factorial(n-1)


def custom_pow(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def sin(x):
    tolerance = .0000000001  # an acceptable tolerance for sin(x)
    sin_result = 0
    term = x  # the current term in taylor series
    sign = 1  # alternate the signe of each term in the series.
    exponent = 1  # exponent of x for each term
    while term >= tolerance or term <= -1*tolerance:  # Adjust the tolerance as needed
        sin_result += term
        sign *= -1
        exponent += 2
        # taylor series implementation
        term = sign * custom_pow(x, exponent) // factorial(exponent)
    return sin_result


def polynomial(x: int, coefficients: list):
    # x is a value we want to calculate in polynomial function
    # number of coefficients shows the degress of our polynomial decreceingly
    degree = len(coefficients) - 1
    result = 0
    for i in range(degree + 1):
        result += coefficients[i] * custom_pow(x, degree - i)
    return result


def sqrt(x):
    # Use the Babylonian or heron method to approximate sqrt(x)
    if x == 0:
        return 0
    elif x < 0:
        return "Square root is not defined for negative numbers."
    precision = .000001
    guess = x
    while True:
        new_guess = (guess + x / guess) / 2
        diff = new_guess - guess
        if diff < 0:
            diff = -diff
        if diff < precision:  # check precision
            return new_guess
        guess = new_guess


# Program input
def UserInput():
    print("Select a function:")
    print("1. sin(x)")
    print("2. x^0.5")
    print("3. Polynomial function")

    function_index = int(input("Enter the function number (1, 2, or 3): "))
    a = int(input("Enter the lower limit (a): "))
    b = int(input("Enter the upper limit (b): "))
    n = int(input("Enter the number of sub-intervals (n): "))

    if function_index == 1:
        selected_function = sin  # a refrence to sin(x) function
    elif function_index == 2:
        selected_function = sqrt  # a refrence to sqrt(x) function
    elif function_index == 3:
        # in here we will call polynomial function
        degree = int(input("Enter the degree of the polynomial: "))
        coefficients = []
        for i in range(degree + 1):
            coefficient = int(
                input(f"Enter the coefficient of x^{degree - i}: "))
            coefficients.append(coefficient)

        def selected_function(x):
            return polynomial(x, coefficients)
    else:
        print("Invalid function number. Please try again.")
        exit()  # we exit the whole program

    integral_result = approximate_integral(selected_function, a, b, n)

    # Display output
    print("Approximate value of the definite integral: ", integral_result)


# UserInput()
