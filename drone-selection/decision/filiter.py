def filter_drones(drones, criteria):
    """
    支持数值区间、严格等值、模糊包含、列表包含等多种筛选
    :param drones: list of dict
    :param criteria: dict，数值型用{"min":x,"max":y}，字符串型直接用str
    :return: list of dict
    """
    def match_value(drone_value, filter_value):
        # 数值区间
        if isinstance(filter_value, dict) and ("min" in filter_value or "max" in filter_value):
            try:
                v = float(drone_value)
                if "min" in filter_value and v < filter_value["min"]:
                    return False
                if "max" in filter_value and v > filter_value["max"]:
                    return False
            except (ValueError, TypeError):
                return False
            return True
        # 严格等值（Yes/No/Cloud/Local）
        elif isinstance(filter_value, str) and filter_value.lower() in ["yes", "no", "cloud", "local"]:
            return str(drone_value).lower() == filter_value.lower()
        # 字符串模糊包含
        elif isinstance(filter_value, str):
            return filter_value.lower() in str(drone_value).lower()
        # 列表包含
        elif isinstance(filter_value, list):
            if isinstance(drone_value, list):
                return any(str(v).lower() in [str(dv).lower() for dv in drone_value] for v in filter_value)
            else:
                return str(drone_value).lower() in [str(v).lower() for v in filter_value]
        return False

    result = []
    for drone in drones:
        match = True
        for key, value in criteria.items():
            if value is None or value == "":
                continue  # 忽略空条件
            if key not in drone or drone[key] is None:
                match = False
                break
            if not match_value(drone[key], value):
                match = False
                break
        if match:
            result.append(drone)
    return result
