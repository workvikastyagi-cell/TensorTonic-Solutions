import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    x = np.asarray(matrix, dtype= np.float64)
    norm = None
    if norm_type == 'l1':
        norm = np.sum(np.abs(x), axis= axis, keepdims= True)
    elif norm_type == 'l2':
        norm = np.sqrt(np.sum(pow(x, 2), axis= axis, keepdims = True))
    else:
        norm = np.max(np.abs(x), axis= axis, keepdims= True)
    return x / np.where(norm == 0, 1, norm)
    pass