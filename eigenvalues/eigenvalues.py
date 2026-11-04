import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype= float)
    eigenvals = np.linalg.eigvals(matrix)
    return np.sort(eigenvals.real)
    pass