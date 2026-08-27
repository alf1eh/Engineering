# Total number of laps
total_laps = 78

# Pit stop time loss (in seconds)
pit_stop_time = 20

# Tyre definitions: base time, degradation per lap, ideal lifespan
tyres = {
    "Soft": {"base_time": 75.0, "deg_per_lap": 0.15, "lifespan": 12},
    "Medium": {"base_time": 80.5, "deg_per_lap": 0.1, "lifespan": 22},
    "Hard": {"base_time": 89.0, "deg_per_lap": 0.07, "lifespan": 35},
}

strategies = {
    "Driver A": [("Medium", 20), ("Hard", 35), ("Hard", 23)],
    "Driver B": [("Hard", 32), ("Medium", 22), ("Hard", 24)]
}

import random

def simulate_driver(strategy):
    lap_times = []
    lap = 0
    
    for tyre_type, stint_length in strategy:
        tyre = tyres[tyre_type]
        
        for i in range(stint_length):
            # Degrade the lap time based on tyre age
            degradation = tyre["deg_per_lap"] * i
            random_variation = random.uniform(-0.2, 0.2)
            lap_time = tyre["base_time"] + degradation + random_variation
            lap_times.append(lap_time)
            lap += 1
            
            if lap >= total_laps:
                break

        # Add pit time if not at race end
        if lap < total_laps:
            lap_times[-1] += pit_stop_time

    return lap_times


#simulating both strategies 
driverA_times = simulate_driver(strategies["Driver A"])
driverB_times = simulate_driver(strategies["Driver B"])

#Calculating total race times 
total_time_A = sum(driverA_times)
total_time_B = sum(driverB_times)

# Display results 
print(f"Driver A total time: {total_time_A:.2f} seconds")
print(f"Driver B total time: {total_time_B:.2f} seconds")

winner = "Driver A" if total_time_A < total_time_B else "Driver B"
print(f"\n🏁 Winner: {winner}")