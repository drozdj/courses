# Visualize and fill missing Power (Watts) dropouts
# %% 
# Import Modules
from fitparse import FitFile
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
from scipy.signal import savgol_filter

# %%
def clean_cadence_data(cadence_array, threshold=51):
    # Create a mask for valid cadence values
    valid_mask = cadence_array > threshold
    
    # Get indices for interpolation
    indices = np.arange(len(cadence_array))
    
    # Interpolate over gaps using valid values
    cleaned_cadence = np.interp(
        indices,
        indices[valid_mask],
        cadence_array[valid_mask]
    )
    
    return cleaned_cadence


# %%
def plot_with_smoothing(fit_file_path, window=_, poly_order=_):
    # Extract data
    power_data = []
    hr_data = []
    cadence_data = []
    timestamps = []
    
    fitfile = FitFile(fit_file_path)
    for record in fitfile.get_messages('record'):
        data = {}
        for data_point in record:
            if data_point.name in ['power', 'heart_rate', 'timestamp','cadence']:
                data[data_point.name] = data_point.value
        
        if 'power' in data:
            power_data.append(data['power'])
        if 'heart_rate' in data:
            hr_data.append(data['heart_rate'])
        if 'timestamp' in data:
            timestamps.append(data['timestamp'])
        if 'cadence' in data:
            cadence_data.append(data['cadence']) 


    # Print data points for debugging
    print(f"Number of data points: Power={len(power_data)}, HR={len(hr_data)}, Cadence={len(cadence_data)}")

    # Convert to numpy arrays
    power_array = np.array(power_data)
    hr_array = np.array(hr_data)
    cadence_array = np.array(cadence_data)
    cadence_array = clean_cadence_data(cadence_array, threshold=10)
    
    # Apply Savitzky-Golay filter for smoothing
    # Window length must be odd and greater than poly_order
    power_smooth = savgol_filter(power_array, window, poly_order)
    hr_smooth = savgol_filter(hr_array, window, poly_order)
    cadence_smooth = savgol_filter(cadence_array, window, poly_order)
    
    # Time axis
    time_in_minutes = [(t - timestamps[0]).total_seconds() / 60 for t in timestamps]
    
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Define heart rate zones
    zones = {
        "Zone 1 (Recovery)": (0, 137),
        "Zone 2 (Aerobic)": (137, 151),
        "Zone 3 (Tempo)": (151, 165),
        "Zone 4 (Threshold)": (165, 172),
        "Zone 5 (VO2 Max)": (172, 220)
    }
    
    # Add heart rate zones as background shapes
    colors = [
        'rgba(144, 238, 144, 0.3)',  # Light green
        'rgba(255, 255, 160, 0.3)',  # Light yellow
        'rgba(255, 160, 122, 0.3)',  # Light salmon
        'rgba(255, 127, 127, 0.3)',  # Light coral
        'rgba(255, 99, 71, 0.3)'     # Tomato red
    ]
   
        # Add cadence array
    fig.add_trace(
        go.Scatter(x=time_in_minutes, y=cadence_smooth, 
                  name="Cadence (Smoothed)", 
                  line=dict(color='purple', width=2)),
        secondary_y=False,
    )


        # Add smoothed power
    fig.add_trace(
        go.Scatter(x=time_in_minutes, y=power_smooth, 
                  name="Power (Smoothed)", 
                  line=dict(color='blue', width=2)),
        secondary_y=False,
    )
    
    # Add smoothed heart rate
    fig.add_trace(
        go.Scatter(x=time_in_minutes, y=hr_smooth, 
                  name="Heart Rate (Smoothed)", 
                  line=dict(color='red', width=2)),
        secondary_y=True,
    )
        # Update power axis
    fig.update_yaxes(
        title_text="Power (watts)", 
        secondary_y=False
    )

    
    for (zone_name, (lower, upper)), color in zip(zones.items(), colors):
        fig.add_shape(
            type="rect",
            x0=min(time_in_minutes),
            x1=max(time_in_minutes),
            y0=lower,
            y1=upper,
            fillcolor=color,
            layer="below",
            line_width=1,                    # Add border width
            line=dict(                       # Add border color
                color='rgba(0,0,0,0.3)',
                dash='dash'                  # Make border dashed
            ),
            secondary_y=True,
        )
        
        # Add zone labels on the right side
        fig.add_annotation(
            x=max(time_in_minutes),
            y=(lower + upper)/2,
            text=zone_name,
            showarrow=False,
            yshift=0,
            xshift=10,
            xanchor="left",
            secondary_y=True,
            font=dict(size=10)
        )
    
    # Update layout to include zones in title
    fig.update_layout(
        title='Power and Heart Rate Analysis with Training Zones',
        xaxis_title='Time (minutes)',
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        )
    )
    
    # Ensure heart rate axis covers all zones
    fig.update_yaxes(
        range=[0, 220],
        secondary_y=True,
        title_text="Heart Rate (bpm)",
        side='right',
        scaleanchor=None,
        scaleratio=None
    )
    
    return fig 

def main():
    fit_file_path = '/Users/drozd/VSCODE/courses/COMS_W4995 /data/raw/7FEC660ABEBD7253_20241127_183353_s.fit'
    # Window size must be odd and greater than poly_order
    fig = plot_with_smoothing(fit_file_path, window=31, poly_order=3)
    fig.show()
    fig.write_html("power_hr_analysis_smoothed.html")

if __name__ == '__main__':
    main()
