def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    sums = {}
    counts = {}
    for cat, t in zip(categories, targets):
        sums[cat] = sums.get(cat, 0.0) + t
        counts[cat] = counts.get(cat, 0) + 1
    means = {cat: sums[cat] / counts[cat] for cat in sums}
    return [means[cat] for cat in categories]
    pass