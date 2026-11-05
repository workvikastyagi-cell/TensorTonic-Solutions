import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x = np.asarray(x)
    rng= np.random.default_rng(seed)
    og_mean = np.mean(x)

    sample_means = []

    for i in range(n_bootstrap):
        sample = rng.choice(x, size = x.shape, replace= True)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)
    sample_means.sort()
    low_pct = ((1-ci)/2) * 100
    up_pct = (ci + ((1 - ci)/ 2)) * 100
    
    low_bound = np.percentile(sample_means, low_pct)
    up_bound = np.percentile(sample_means, up_pct)

    return {
        'bootstrap_mean': np.mean(np.asarray(sample_means)),
        'lower': low_bound,
        'upper': up_bound
    }
    pass