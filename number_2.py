# factorial func
def factorial(number):
    if (number == 1) or (number == 0):
        return 1

    return number * factorial(number - 1)


def close_fact_less_than(num):
    # returns the closest fact less than the specefic number
    i = 0
    fact = factorial(i)
    while fact <= num:
        i += 1
        fact = factorial(i)

    return i - 1


def cantor_expansion(num):
    cantors_list = []
    while num > 1:
        temp = close_fact_less_than(num)
        cantors_list.append(temp)
        num = num - factorial(temp)
    else:
        cantors_list.append(1)
    return cantors_list


def UserInput():
    print('Eg: 115 = 4(4!) + 3(3!) + 1!')
    #  get date from user and display  it as a nice human readable line
    user_input = int(
        input("Enter a number you want to see the cantor expansion of :"))
    factors = cantor_expansion(user_input)
    result = f"{user_input} = "
    i = 0
    while i < len(factors):
        factor = factors[i]
        if i > 0:
            result += " + "
        result += f"{factor}({factor}!)"
        i += 1
    print(result)


# UserInput()
