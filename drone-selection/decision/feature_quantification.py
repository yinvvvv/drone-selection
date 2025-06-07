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

        if "regular_maintenance_complexity" in drone:
            complexity = drone["regular_maintenance_complexity"].lower()
            if complexity == "low":
                drone["regular_maintenance_complexity"] = 3
            elif complexity == "medium":
                drone["regular_maintenance_complexity"] = 2
            elif complexity == "high":
                drone["regular_maintenance_complexity"] = 1
            else:
                drone["regular_maintenance_complexity"] = 0

        if "transmission_capability" in drone:
            capability = drone["transmission_capability"].lower()
            if capability == "yes/cloud":
                drone["transmission_capability"] = 4
            elif capability == "yes/local":
                drone["transmission_capability"] = 3
            elif capability == "no/cloud":
                drone["transmission_capability"] = 2
            elif capability == "no/local":
                drone["transmission_capability"] = 1
            else:
                drone["transmission_capability"] = 0

        if "supported_mission_types" in drone:
            mission_types = drone["supported_mission_types"]
            if mission_types:
                drone["supported_mission_types"] = len(mission_types.split(","))
            else:
                drone["supported_mission_types"] = 0

        if "sensor_support" in drone:
            sensor_types = drone["sensor_support"]
            if sensor_types:
                drone["sensor_support"] = len(sensor_types.split(","))
            else:
                drone["sensor_support"] = 0

    return drones
            
