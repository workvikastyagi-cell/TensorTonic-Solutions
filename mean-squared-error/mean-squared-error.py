import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    # Write code here
    yp = np.asarray(y_pred, dtype= float)
    yt = np.asarray(y_true, dtype= float)
    mse = np.mean((yp - yt) ** 2)
    return float(mse)
    pass