def wsm(data, weights):
    """
    Weighted Sum Model (WSM) for ranking drones.
    """
    scores = data.dot(weights)
    return scores
