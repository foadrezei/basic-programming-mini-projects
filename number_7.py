def stringMaking():
    n = int(input("Enter the number of characters: "))
    characters = input("Enter the characters separated by spaces: ").split()
    result = []
    for length in range(1, n + 1):
        # since allStringCombinations returns a list of strings we can iterate over it
        for combination in allStringCombinations(characters, length):
            result.append(''.join(combination))
    return result


# a recurcive function to get all compinations that we want
def allStringCombinations(characters, length):
    # our base case
    if length == 1:
        # we use list comprehension in here to be more clean
        result = []
        for char in characters:
            result.append((char,))
        return result
    else:
        result = []
        # here we have recursion
        smaller_combinations = allStringCombinations(characters, length - 1)
        for char in characters:
            for smaller_comb in smaller_combinations:

                if char not in smaller_comb:  # in here we make sure of no reapeted charecters
                    result.append((char,) + smaller_comb)
        return result


def UserInput():
    output = stringMaking()
    for string in output:
        print(string, end='   ')


# UserInput()
