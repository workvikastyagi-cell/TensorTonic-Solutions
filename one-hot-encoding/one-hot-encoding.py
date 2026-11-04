import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    y  = np.asarray(y, dtype= int)
    if num_classes is None:
        # If num classes are not given, calculate
        num_classes = int(np.max(y)) + 1
    # Create a sparse matrix of y rows, num_class cols
    encoded = np.zeros((y.size, num_classes), dtype = float)
    
    encoded[np.arange(y.size), y] = 1.0
    return encoded