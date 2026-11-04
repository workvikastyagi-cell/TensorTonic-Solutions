
import numpy as np

def matrix_inverse(A):
    A = np.array(A, dtype=float)
    n = len(A)

    # Add identity matrix to the right
    identity = np.eye(n)
    matrix = np.concatenate((A, identity), axis=1)

    # Process each column
    for i in range(n):

        # Find a row with a non-zero pivot
        if abs(matrix[i, i]) < 1e-12:
            for j in range(i + 1, n):
                if abs(matrix[j, i]) > 1e-12:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
            else:
                return None

        # Make pivot equal to 1
        matrix[i] = matrix[i] / matrix[i, i]

        # Make other values in this column zero
        for j in range(n):
            if i != j:
                factor = matrix[j, i]
                matrix[j] = matrix[j] - factor * matrix[i]

    # Return the right half
    return matrix[:, n:]
