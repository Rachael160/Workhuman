# Author: Rachael Kelly

import json
import math

# Function to calculate two coordinate difference
def calculate_distance(lat, lon, lat2, lon2):
    # Radius of earth in km
    earth_rad = 6371.0

    # Convert degrees to radians using math.radian method
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula (provide)
    dlon = lon2_rad - lon_rad
    dlat = lat2_rad - lat_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat_rad) * math.cos(lat_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    #find the distance 
    distance = earth_rad * c
    return distance

# Coordinates of St Stephens Green
green_lat = 53.337839
green_lon = -6.259520

# Read the list of friends from the text file
friend_invitation = []

with open('friends.txt', 'r') as file:
    for line in file:
        friend_data = json.loads(line)
        
        # make sure the variables are floats 
        friend_lat = float(friend_data['latitude'])
        friend_lon = float(friend_data['longitude'])

        # Check if the friend is within 100km
        distance = calculate_distance(
            green_lat, green_lon,
            friend_lat, friend_lon
        )

        if distance <= 100:
            friend_invitation.append(friend_data)

# Sort the friends by id in ascending order
friend_invitation.sort(key=lambda x: x['user_id'])

# Print names and user ids of invited friends
for friend in friend_invitation:
    print(f"User ID: {friend['user_id']}, Name: {friend['name']}")
