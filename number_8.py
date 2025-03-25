def evaluate_prefix_expression(expression: str):
    # Initialize an empty stack
    stack = []

    # Read the expression from right to left
    for item in expression[::-1]:
        if item.isdigit():  # if item(operand) is number -> push it into stack
            stack.append(int(item))
        else:  # pop the top two operands from the stack.
            # Perform the operation using the operator with 2 operands.

            operand1 = stack.pop()
            operand2 = stack.pop()

            if item == '+':
                result = operand1 + operand2
            elif item == '-':
                result = operand1 - operand2
            elif item == '*':
                result = operand1 * operand2
            elif item == '/':
                result = operand1 / operand2
            elif item == '//':
                result = operand1 // operand2
            elif item == '**':
                result = operand1 ** operand2

            stack.append(result)  # Push the result back onto the stack.

    return stack[0]


# user input section
def UserInput():
    print('for example: `∗+23−94` ')
    expression = input("Enter a prefix arithmetic expression:  ")

    result = evaluate_prefix_expression(expression)
    print("Result:", result)
# UserInput()