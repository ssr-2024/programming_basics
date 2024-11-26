
import json
import numpy as np
from matplotlib.figure import SubplotParams
import matplotlib.pyplot as plt
import pyemgpipeline as pep

# Load the JSON data
with open('C:\\ssr\\programming_basics\\wiki\\emg_trial.json', 'r') as file:
    data = json.load(file)

# Function to extract channel data from JSON
def extract_channel_data_from_json(data):
    """
    Extracts channel data from JSON data and returns the data and channel names.

    Parameters:
    - data: The JSON data loaded as a Python data structure (e.g., list of dictionaries).

    Returns:
    - all_data: A 2D matrix of the extracted channel data.
    - channel_names: A list of channel names.

    Raises:
    - ValueError: If no valid channel data is found in the JSON.
    """
    channel_data_list = []
    channel_names = []

    for entry in data:
        items = entry.get('items', [])
        for item in items:
            payload = item.get('payload')
            if payload and 'channels' in payload:
                if not channel_names:  # Set channel names only once
                    channel_names = list(payload['channels'].keys())
                channel_matrix = np.column_stack([np.array(payload['channels'][key]) for key in payload['channels'].keys()])
                channel_data_list.append(channel_matrix)
            else:
                print("No 'payload' or 'channels' in this 'item':", item)  # Debug output

    if channel_data_list:
        all_data = np.vstack(channel_data_list)
    else:
        raise ValueError("No valid channel data found in the JSON")

    return all_data, channel_names

# Call the function
all_data, channel_names = extract_channel_data_from_json(data)

# For further processing as a list of arrays
all_data_list = [all_data]  # Adapt if multiple trials are present

# Set plot parameters
emg_plot_params = pep.plots.EMGPlotParams(
    n_rows=1,
    n_cols=all_data.shape[1],  # Number of channels as columns
    fig_kwargs={
        'figsize': (16, 1.2),
        'subplotpars': SubplotParams(top=0.7, wspace=0.1, hspace=0),
    },
    line2d_kwargs={
        'color': 'b',
    },
)

# Create the EMGMeasurementCollection
sample_rate = 500  # Adjust based on the actual sample rate in data
trial_names = ['Trial 1']
c = pep.wrappers.EMGMeasurementCollection(
    all_data_list, 
    hz=sample_rate, 
    trial_names=trial_names, 
    channel_names=channel_names, 
    emg_plot_params=emg_plot_params
)

# Apply processing steps
c.apply_dc_offset_remover()
c.apply_bandpass_filter(bf_order=4, bf_cutoff_fq_lo=10, bf_cutoff_fq_hi=200)
c.apply_full_wave_rectifier()
c.apply_linear_envelope(le_order=4, le_cutoff_fq=6)
c.apply_end_frame_cutter(n_end_frames=30)
max_amplitude = c.find_max_amplitude_of_each_channel_across_trials()
c.apply_amplitude_normalizer(max_amplitude)

# Plot the results
c.plot()
plt.draw()  # Force a render

# Save the plot as a .jpeg file
plt.savefig('C:/ssr/programming_basics/wiki/processed_emg_plot.jpeg')
