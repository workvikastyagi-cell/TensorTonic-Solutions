import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    prob = math.exp(-lam)
    cdf = prob
    for i in range(1, k+1):
        prob *= lam / i
        cdf += prob
    pmf = prob
    return {"pmf": pmf, "cdf": cdf}
    pass