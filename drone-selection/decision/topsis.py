import numpy as np


def calculate_topsis(criteria_weights, drones):
    """
    使用 TOPSIS 模型计算无人机评分
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

    # 第一步：标准化决策矩阵（向量标准化）
    normalized_matrix = matrix / np.sqrt(np.sum(matrix ** 2, axis=0))

    # 第二步：计算加权标准化矩阵
    weights = np.array(list(criteria_weights.values()))
    weighted_matrix = normalized_matrix * weights

    # 第三步：确定正理想解和负理想解
    reverse_criteria = ["drone_cost", "startup_time"]
    positive_ideal = np.zeros(len(criteria_weights))
    negative_ideal = np.zeros(len(criteria_weights))

    for i, key in enumerate(criteria_weights.keys()):
        if key in reverse_criteria:
            # 对于成本型指标，正理想解是最小值，负理想解是最大值
            positive_ideal[i] = weighted_matrix[:, i].min()
            negative_ideal[i] = weighted_matrix[:, i].max()
        else:
            # 对于效益型指标，正理想解是最大值，负理想解是最小值
            positive_ideal[i] = weighted_matrix[:, i].max()
            negative_ideal[i] = weighted_matrix[:, i].min()

    # 第四步：计算到理想解的距离
    distance_to_positive = np.sqrt(np.sum((weighted_matrix - positive_ideal) ** 2, axis=1))
    distance_to_negative = np.sqrt(np.sum((weighted_matrix - negative_ideal) ** 2, axis=1))

    # 第五步：计算相对接近度
    scores = distance_to_negative / (distance_to_positive + distance_to_negative + 1e-9)

    # 生成结果
    result = [{"name": drones[i]["name"], "score": scores[i]} for i in range(len(drones))]
    result.sort(key=lambda x: x["score"], reverse=True)

    return result
