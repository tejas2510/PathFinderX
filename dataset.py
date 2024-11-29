import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Constants
num_flights = 50            # Number of unique flights, adjusted for max 20,000 rows
interval_seconds = 20       # Time interval in seconds
departure_airport = "BOM"   # Fixed departure
arrival_airport = "GAU"     # Fixed arrival (Assam, Guwahati)
start_time = datetime(2024, 1, 1)  # Start time for the dataset
max_total_rows = 20000      # Target maximum rows

# Geographical ranges for realistic lat/long paths
departure_coords = (19.0886, 72.8676)  # Approximate coordinates for BOM (lat, lon)
arrival_coords = (26.1445, 91.7362)    # Approximate coordinates for GAU (lat, lon)
cruise_altitude = 35000                # Typical cruise altitude in feet
heading_change = 5                     # Small incremental heading changes

# List of airline names and codes
airline_names = ["Air India", "IndiGo", "SpiceJet", "GoAir", "Vistara", "AirAsia"]
airline_codes = ["AI", "6E", "SG", "G8", "UK", "AK"]

# Straight-line interpolation for latitude and longitude
def interpolate_straight_coords(start, end, steps):
    lat_diff = (end[0] - start[0]) / steps
    lon_diff = (end[1] - start[1]) / steps
    
    path_coords = []
    for i in range(steps):
        lat = start[0] + i * lat_diff
        lon = start[1] + i * lon_diff
        path_coords.append((lat, lon))
        
    return path_coords

# Adjust maximum records per flight to fit under 20,000 rows
records_per_flight = max_total_rows // num_flights

# Generate data for each flight
data = []
for i in range(num_flights):
    # Randomly select an airline name and code
    airline_index = np.random.randint(len(airline_names))
    airline_name = airline_names[airline_index]
    airline_code = airline_codes[airline_index]
    flight_number = f"{airline_name}_{airline_code}{np.random.randint(1000, 9999)}"  # Realistic flight number format
    timestamp = start_time
    
    # Generate a realistic flight duration in 20-sec intervals with a random adjustment
    current_records = np.random.randint(records_per_flight - 50, records_per_flight + 50)  # Small variability
    takeoff_duration = int(current_records * 0.1)       # 10% of the flight time for ascent
    cruise_duration = int(current_records * 0.8)        # 80% of the flight time for cruising
    landing_duration = current_records - takeoff_duration - cruise_duration
    
    # Generate a straight path of latitude and longitude coordinates
    coords = interpolate_straight_coords(departure_coords, arrival_coords, current_records)
    
    # Initial heading for the flight (toward GAU from BOM)
    heading = np.degrees(np.arctan2(
        arrival_coords[1] - departure_coords[1],
        arrival_coords[0] - departure_coords[0]
    )) % 360  # Convert to degrees and wrap within 0-360
    
    # Disturbances during cruising
    disturbance_intervals = np.random.choice(range(takeoff_duration, takeoff_duration + cruise_duration), size=5, replace=False)
    disturbance_magnitude = 500  # Altitude drop in feet
    
    for j in range(current_records):
        # Interpolated latitude and longitude
        latitude, longitude = coords[j]
        
        # Simulate altitude profile with small disturbances during cruise
        if j < takeoff_duration:
            altitude = int(cruise_altitude * (j / takeoff_duration) * np.random.uniform(0.95, 1.05))
        elif j < takeoff_duration + cruise_duration:
            altitude = cruise_altitude + (np.random.choice([-disturbance_magnitude, disturbance_magnitude]) 
                                          if j in disturbance_intervals else np.random.randint(-100, 100))
        else:
            descent_stage = j - (takeoff_duration + cruise_duration)
            altitude = int(cruise_altitude * (1 - descent_stage / landing_duration) * np.random.uniform(0.95, 1.05))
        
        # Adjust heading gradually
        heading += np.random.uniform(-heading_change, heading_change)
        heading = heading % 360  # Keep heading within 0-360 degrees
        
        # Add record for the current timestamp
        data.append({
            "flight_number": flight_number,
            "latitude": latitude,
            "longitude": longitude,
            "heading": heading,
            "altitude": altitude,
            "departure": departure_airport,
            "arrival": arrival_airport,
            "timestamp": timestamp
        })
        
        # Increment timestamp by the interval (20 seconds)
        timestamp += timedelta(seconds=interval_seconds)
    
    # Check if max rows reached
    if len(data) >= max_total_rows:
        break

# Trim excess rows if any
df = pd.DataFrame(data[:max_total_rows])

# Save to CSV (optional)
df.to_csv("flight_data_bom_to_gau.csv", index=False)

# Show sample data
print(df.head())
