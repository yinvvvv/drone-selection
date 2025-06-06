def topsis(data, weights):
    """
    Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for ranking drones.
    """
    # Step 6.1: Normalize the data
    normalized_data = data / np.sqrt((data ** 2).sum(axis=0))
    
    # Step 6.2: Weighted normalized data
    weighted_data = normalized_data * weights
    
    # Step 6.3: Determine ideal and anti-ideal solutions
    ideal_solution = weighted_data.max(axis=0)
    anti_ideal_solution = weighted_data.min(axis=0)
    
    # Step 6.4: Calculate distances to ideal and anti-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
    distance_to_anti_ideal = np.sqrt(((weighted_data - anti_ideal_solution) ** 2).sum(axis=1))
    
    # Step 6.5: Calculate the TOPSIS score
    scores = distance_to_anti_ideal / (distance_to_ideal + distance_to_anti_ideal)
    return scores
