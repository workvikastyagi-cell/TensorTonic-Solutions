import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    cdf = 0.0
    for i in range(k+1):
        pmf = (math.comb(n,i) * p ** i) * (1 - p) ** (n - i)
        cdf += pmf
    return {'pmf': float(pmf), "cdf": float(cdf)}
    pass