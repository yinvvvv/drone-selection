import numpy as np

def calculate_ahp(criteria_weights, drones):
    """
    使用 AHP 模型计算无人机评分 (包含 Min-Max 归一化)
    :param criteria_weights: dict (特征的权重，key 为特征名称，value 为权重)
    :param drones: list of dict (无人机数据，已量化)
    :return: list of dict (评分和排名)
    """
    # 移除 "compliance" 特征
    criteria_weights = {key: value for key, value in criteria_weights.items() if key != "compliance"}

    # 构建决策矩阵
    matrix = []
    for drone in drones:
        row = []
        for key in criteria_weights.keys():
            value = drone.get(key, 0)
            row.append(float(value))
        matrix.append(row)

    matrix = np.array(matrix)

    min_values = matrix.min(axis=0)
    max_values = matrix.max(axis=0)

    reverse_criteria = ["drone_cost", "startup_time"]
    for i, key in enumerate(criteria_weights.keys()):
        if key in reverse_criteria:
            matrix[:, i] = (max_values[i] - matrix[:, i]) / (max_values[i] - min_values[i] + 1e-9)
        else:
            matrix[:, i] = (matrix[:, i] - min_values[i]) / (max_values[i] - min_values[i] + 1e-9)

    weights = np.array(list(criteria_weights.values()))
    scores = matrix.dot(weights)
    result = [{"name": drones[i]["name"], "score": scores[i]} for i in range(len(drones))]

    result.sort(key=lambda x: x["score"], reverse=True)
    return result
