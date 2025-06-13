import numpy as np

def calculate_wsm(criteria_weights, drones):
    """
    使用 WSM (Weighted Sum Model) 计算无人机评分
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
    
    # Min-Max 归一化
    min_values = matrix.min(axis=0)
    max_values = matrix.max(axis=0)
    
    # 对于成本型指标（越小越好）进行反向归一化
    reverse_criteria = ["drone_cost", "startup_time"]
    normalized_matrix = np.zeros_like(matrix)
    
    for i, key in enumerate(criteria_weights.keys()):
        if key in reverse_criteria:
            # 成本型指标：归一化后取反
            normalized_matrix[:, i] = (max_values[i] - matrix[:, i]) / (max_values[i] - min_values[i] + 1e-9)
        else:
            # 效益型指标：正常归一化
            normalized_matrix[:, i] = (matrix[:, i] - min_values[i]) / (max_values[i] - min_values[i] + 1e-9)
    
    # WSM 加权求和
    weights = np.array(list(criteria_weights.values()))
    scores = normalized_matrix.dot(weights)
    
    # 生成结果
    result = [{"name": drones[i]["name"], "score": scores[i]} for i in range(len(drones))]
    result.sort(key=lambda x: x["score"], reverse=True)
    
    return result