#
# %%
import gpxpy
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def extract_data_with_averages(gpx_file):
    data = []
    with open(gpx_file, 'r') as file:
        gpx = gpxpy.parse(file)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    power = point.extensions[0].text if point.extensions else None
                    cadence = point.extensions[1].find('{*}cad').text if point.extensions else None
                    hr = point.extensions[1].find('{*}hr').text if point.extensions else None
                    
                    data.append({
                        'timestamp': point.time,
                        'power': float(power) if power else 0,
                        'cadence': float(cadence) if cadence else 0,
                        'heart_rate': float(hr) if hr else 0
                    })
    
    df = pd.DataFrame(data)
    
    # Calculate rolling averages
    df['power_5s_avg'] = df['power'].rolling(window=5, min_periods=1).mean()
    df['cadence_5s_avg'] = df['cadence'].rolling(window=5, min_periods=1).mean()
    df['heart_rate_5s_avg'] = df['heart_rate'].rolling(window=5, min_periods=1).mean()
    
    return df

def create_power_cadence_hr_plot(df):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add power trace
    fig.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['power_5s_avg'],
            name="Power (5s avg)",
            line=dict(color='#FF4B4B', width=1)
        ),
        secondary_y=False
    )

    # Add cadence trace
    fig.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['cadence_5s_avg'],
            name="Cadence (5s avg)",
            line=dict(color='#2E5CEA', width=1)
        ),
        secondary_y=True
    )

    # Add heart rate trace
    fig.add_trace(
        go.Scatter(
            x=df['timestamp'],
            y=df['heart_rate_5s_avg'],
            name="Heart Rate (5s avg)",
            line=dict(color='#00CC96', width=1)
        ),
        secondary_y=True
    )

    fig.update_layout(
        title='Power, Cadence, and Heart Rate Over Time',
        template='plotly_dark',
        hovermode='x unified',
        showlegend=True
    )

    fig.update_yaxes(title_text="Power (watts)", secondary_y=False)
    fig.update_yaxes(title_text="Cadence (rpm) / Heart Rate (bpm)", secondary_y=True)
    
    return fig

# Usage
file_path = 'drozdj/GOTOES_3145244675478618.gpx'
df = extract_data_with_averages(file_path)
fig = create_power_cadence_hr_plot(df)
fig.show()
