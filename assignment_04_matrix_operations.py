# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: 2D Lists (Matrices), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# This program performs:
# A. Matrix Transpose
# B. Matrix Addition
# C. Matrix Multiplication
#
# =============================================================================


# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------

def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = []

    for column in range(columns):
        new_row = []

        for row in range(rows):
            new_row.append(matrix[row][column])

        transposed_matrix.append(new_row)

    return transposed_matrix


# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    columns = len(matrix_a[0])

    result = []

    for row in range(rows):
        new_row = []

        for column in range(columns):
            value = matrix_a[row][column] + matrix_b[row][column]
            new_row.append(value)

        result.append(new_row)

    return result


# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    columns_a = len(matrix_a[0])
    columns_b = len(matrix_b[0])

    result = []

    for row in range(rows_a):
        new_row = []

        for column in range(columns_b):
            total = 0

            for k in range(columns_a):
                total += matrix_a[row][k] * matrix_b[k][column]

            new_row.append(total)

        result.append(new_row)

    return result


# -----------------------------------------------------------------------------
# FUNCTION TO READ A MATRIX
# -----------------------------------------------------------------------------

def read_matrix(rows, columns):
    matrix = []

    for row in range(rows):
        while True:
            values = input(f"Enter row {row + 1}: ").split()

            if len(values) == columns:
                new_row = []

                for value in values:
                    new_row.append(float(value))

                matrix.append(new_row)
                break
            else:
                print(f"Error: Please enter exactly {columns} values.")

    return matrix


# -----------------------------------------------------------------------------
# FUNCTION TO DISPLAY A MATRIX
# -----------------------------------------------------------------------------

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:g}", end="\t")
        print()


# =============================================================================
# MAIN PROGRAM
# =============================================================================

if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # PART A — TRANSPOSE A MATRIX
    # -------------------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PART A — TRANSPOSE A MATRIX")
    print("=" * 60)

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, columns)

    transposed_matrix = transpose_matrix(matrix)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transposed_matrix)


    # -------------------------------------------------------------------------
    # PART B — ADD TWO MATRICES
    # -------------------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PART B — ADD TWO MATRICES")
    print("=" * 60)

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix(rows, columns)

    print("\nEnter values for Matrix B:")
    matrix_b = read_matrix(rows, columns)

    sum_matrix = add_matrices(matrix_a, matrix_b)

    print("\nMatrix A:")
    display_matrix(matrix_a)

    print("\nMatrix B:")
    display_matrix(matrix_b)

    print("\nA + B:")
    display_matrix(sum_matrix)


    # -------------------------------------------------------------------------
    # PART C — MULTIPLY TWO MATRICES
    # -------------------------------------------------------------------------

    print("\n" + "=" * 60)
    print("PART C — MULTIPLY TWO MATRICES")
    print("=" * 60)

    rows_a = int(input("Enter number of rows for Matrix A: "))
    columns_a = int(input("Enter number of columns for Matrix A: "))

    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix(rows_a, columns_a)

    rows_b = int(input("Enter number of rows for Matrix B: "))
    columns_b = int(input("Enter number of columns for Matrix B: "))

    if columns_a != rows_b:
        print("\nError: The number of columns in Matrix A must equal")
        print("the number of rows in Matrix B.")
    else:
        print("\nEnter values for Matrix B:")
        matrix_b = read_matrix(rows_b, columns_b)

        product_matrix = multiply_matrices(matrix_a, matrix_b)

        print("\nMatrix A:")
        display_matrix(matrix_a)

        print("\nMatrix B:")
        display_matrix(matrix_b)

        print("\nA × B:")
        display_matrix(product_matrix)