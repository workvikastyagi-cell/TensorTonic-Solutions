import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.asarray(x, dtype= float)
    mean = np.mean(x)
    centered = x - mean
    n = x.shape[0]
    var = np.sum(centered ** 2) / (n - 1)
    std = var ** 0.5

    std_err = std / (n ** 0.5)

    t_val = (mean - mu0) / std_err

    return float(t_val)
    pass