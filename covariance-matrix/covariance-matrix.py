import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    centered = X - np.mean(X, axis= 0)
    cov = (centered.T @ centered) / (X.shape[0] - 1)

    return cov
    pass