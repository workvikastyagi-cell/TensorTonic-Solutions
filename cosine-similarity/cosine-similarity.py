import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    a_n = np.linalg.norm(a)
    b_n = np.linalg.norm(b)

    if a_n == 0 or b_n == 0:
        return 0.0
    res = np.dot(a, b) / (a_n * b_n)
    return float(res)
    pass