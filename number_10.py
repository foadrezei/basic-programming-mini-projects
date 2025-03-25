def determinant(matrix):
    # Base case for 2*2 matrix
    if len(matrix) == 2:
        # the determinant for 2*2 matricx is ad-bc [[a,b],[c,d]]
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(len(matrix)):

        # sub-matrix that removs the first row and the i-th column from the original matrix.
        sub_matrix = []
        # loops from the second row becuse the first row is removed
        for j in range(1, len(matrix)):
            minor_row = []
            for k in range(len(matrix)):
                if k != i:
                    minor_row.append(matrix[j][k])
            sub_matrix.append(minor_row)
            # matrix[0][i] : the i-th element in the first row of the original matrix
        det += ((-1) ** i) * matrix[0][i] * \
            determinant(sub_matrix)  # recirsion

    return det


def cramer_rule(matrix_A, vector_b):
    n = len(matrix_A)  # Get the size of the matrix
    det_A = determinant(matrix_A)  # Calculate the determinant of matrix_A

    # Check if the determinant is 0
    if det_A == 0:
        print("The determinant of the given matrix is 0, and we have no answer for that")
        return None

    results = []

    for i in range(n):
        # Create a copy of matrix_A
        A_i = [row[:] for row in matrix_A]

        # Replace the i-th column of A_i with vector_b
        for j in range(n):
            A_i[j][i] = vector_b[j]

        # Calculate the determinant of A_i
        det_A_i = determinant(A_i)

        # Calculate the result for the i-th variable
        result_i = det_A_i / det_A

        # Add the result to the results list
        results.append(result_i)

    return results


# Prompt the user to enter the matrix A
def UserInput():
    print("Enter the matrix A:")
    matrix_A = []
    num_rows = int(input("Enter the number of rows: "))
    for _ in range(num_rows):
        row = []
        elements = input(
            "Enter the elements of the row separated by spaces: ").split()
        for element in elements:
            row.append(int(element))
        matrix_A.append(row)

    # Prompt the user to enter the vector b
    print("Enter the vector b:")
    vector_b = []
    elements = input(
        "Enter the elements of the vector separated by spaces: ").split()
    for element in elements:
        vector_b.append(int(element))

    # Solve the system of linear equations
    solution = cramer_rule(matrix_A, vector_b)
    print("The solution is:", solution)


# UserInput()
