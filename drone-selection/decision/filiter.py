def filter_drones(drones, criteria):
    """
    支持数值型区间筛选和字符串包含筛选
    :param drones: list of dict
    :param criteria: dict，数值型用{"min":x,"max":y}，字符串型直接用str
    :return: list of dict
    """
    result = []
    for drone in drones:
        match = True
        for key, value in criteria.items():
            if value is None or value == "":
                continue  # Ignore empty criteria
            if key not in drone:
                match = False
                break
            # 数值区间
            if isinstance(value, dict) and ("min" in value or "max" in value):
                try:
                    v = float(drone[key])
                    if "min" in value and v < value["min"]:
                        match = False
                        break
                    if "max" in value and v > value["max"]:
                        match = False
                        break
                except ValueError:
                    match = False
                    break
            # 字符串包含
            elif isinstance(value, str):
                if value.lower() not in str(drone[key]).lower():
                    match = False
                    break
        if match:
            result.append(drone)
    return result
