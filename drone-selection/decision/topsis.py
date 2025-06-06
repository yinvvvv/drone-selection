def topsis(data, weights):
    """
    Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for ranking drones.
    """
    normalized_data = data / np.sqrt((data ** 2).sum(axis=0))
  
    weighted_data = normalized_data * weights
    
    ideal_solution = weighted_data.max(axis=0)
    anti_ideal_solution = weighted_data.min(axis=0)
    
    # Calculate distances to ideal and anti-ideal solutions
    distance_to_ideal = np.sqrt(((weighted_data - ideal_solution) ** 2).sum(axis=1))
    distance_to_anti_ideal = np.sqrt(((weighted_data - anti_ideal_solution) ** 2).sum(axis=1))
    
    # Calculate the TOPSIS score
    scores = distance_to_anti_ideal / (distance_to_ideal + distance_to_anti_ideal)
    return scores
