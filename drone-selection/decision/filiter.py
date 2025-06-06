def filter_drones(data, criteria):
    """
    Filter drones based on user input criteria.
    """
    for key, value in criteria.items():
        if isinstance(value, (int, float)):
            data = data[data[key] >= value]
        elif isinstance(value, str):
            data = data[data[key] == value]
    return data
