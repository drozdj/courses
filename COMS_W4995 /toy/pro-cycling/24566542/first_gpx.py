# 2017 99a Coppa Bernocchi - 42o GP BPM.gpx 
# %% Import Modules
import gpxpy
import pandas as pd

# %% 
# Open and parse the GPX file
with open('gpx_before_dem/2017 99a Coppa Bernocchi - 42o GP BPM.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Access track points
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print(f'Point at ({point.latitude},{point.longitude}) -> {point.elevation}')

# %% 
gpx_points = gpx.tracks[0].segments[0].points
data = []
for point in gpx_points:
    data.append({
        'lon': point.longitude,
        'lat': point.latitude,
        'elev': point.elevation,
        'time': point.time
    })
df = pd.DataFrame(data)

# %% 