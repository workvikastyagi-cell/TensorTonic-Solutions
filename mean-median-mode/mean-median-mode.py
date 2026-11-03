from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x).most_common(1)[0][0]

    return {'mean': float(mean), 'median': float(median), 'mode': float(mode)}
    pass