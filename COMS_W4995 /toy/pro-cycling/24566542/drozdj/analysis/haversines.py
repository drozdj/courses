# 
# %%
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c


# Usage
gpx_file = 'gpx_files/GOTOES_6517688740011329.gpx'
distance = haversine(lon1=11.549425125122,
                     lat1=43.085964202881,
                     lon2=11.489450454712,
                     lat2=43.137748718262)


print(f"Total distance: {distance:.2f} km")
