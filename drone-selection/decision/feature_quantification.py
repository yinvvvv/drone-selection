def quantify_features(drones):
  """
    Quantize non-numerical features to numerical values ​​for model calculation
    :param drones: list of dict (drone data)
    :return: list of dict (quantized drone data)
  """
  for drone in drones:
        if "night_flight_support" in drone:
            drone["night_flight_support"] = 1 if drone["night_flight_support"].lower() == "yes" else 0

        if "auto_nav_obstacle_avoid" in drone:
            drone["auto_nav_obstacle_avoid"] = 1 if drone["auto_nav_obstacle_avoid"].lower() == "yes" else 0
