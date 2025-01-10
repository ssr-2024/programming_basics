# Pyemgpipeline
Or how to hopefully process EMG-data as simple as possible (in a world where deadlifts are made as complicated as possible.)

## Abstract 
<u> What is *pyemgpipeline*?</u>

*pyemgpipeline* is an electromyography (EMG) signal processing pipeline package. It implements internationally accepted EMG processing conventions and provides a high-level interface for ensuring user adherence to those conventions, in terms of (1) processing parameter values, (2) processing steps, and (3) processing step order. It is suitable for both surface EMG and intramuscular EMG.  
This document aims to explain step by step how *pyemgpipeline* can be applied to process EMG-data captured via Streamix (smx).

<div style="border: 2px solid #0073e6; background-color: #e6f7ff; padding: 10px; border-radius: 5px; color: #333333;">
Further information about <i>pyemgpipeline</i> can be found here:
<a href="https://aalhossary.github.io/pyemgpipeline/index.html" style="color: #0056b3;">https://aalhossary.github.io/pyemgpipeline/index.html</a>
</div>


## Table of contents
- [Abstract](#abstract)
- [Practical relevance](#practical-relevance)
- [Tutorial](#tutorial)
  - [1. Installation](#1-installation)
  - [2. Data preparation](#2-data-preparation)
      - [*1st* of all](#1st-of-all)
      - [*2nd* of all](#2nd-of-all)
      - [*3rd* of all](#3rd-of-all)
      - [*4th* of all](#4th-of-all)
      - [*Last* of all](#last-of-all)
  - [3. Data processing](#3-data-processing)
      - [Step 1: DC offset removal](#step-1-dc-offset-removal)
      - [Step 2: Bandpass filtering.](#step-2-bandpass-filtering)
      - [Step 3: Full wave rectification](#step-3-full-wave-rectification)
      - [Step 4: Linear envelope](#step-4-linear-envelope)
      - [Step 5: End frame cutting](#step-5-end-frame-cutting)
      - [Step 6: Amplitude normalization](#step-6-amplitude-normalization)
      - [Step 7: Segmentation](#step-7-segmentation)
  - [4. Plot and save data](#4-plot-and-save-data)
- [Theory to practice](#theory-to-practice)

---

## Practical relevance 
    
To capture EMG data, the ISPW uses MyonEMG, a hardware system for capturing and wireless transmitting of surface EMG sensor signals.  
Since data recordings in the ISPW labs now are performed using the Streamix-application, the MyonEMG hardware has been adjusted to connect and be integrated into Streamix, with the ultimate goal to easily incorporate EMG-measurements into research projects. However, raw EMG-signals are difficult to interpret, possibly contain noise signals and other interferences.  
This is where <u>*pyemgpipeline*</u> becomes interesting as a simple tool to process the Streamix-captured EMG-data and thereby simplify the lab workflow.


<div style="border: 2px solid #0073e6; background-color: #e6f7ff; padding: 10px; border-radius: 5px; color: #333333;">
More in-depth information about MyonEMG can be found here:
<a href="https://ttl.tek.sdu.dk/wiki/images/8/87/M320_user_manual_V1.7.pdf " style="color: #0056b3;">https://ttl.tek.sdu.dk/wiki/images/8/87/M320_user_manual_V1.7.pdf l</a>
</div>

## Tutorial 

### 1. Installation
pyemgpipeline can be installed from the PyPI repository:

    pip install pyemgpipeline

The dependencies of this package include numpy, scipy, and matplotlib.

After installation, the package can be launched by:

    >>> import pyemgpipeline as pep

For the entire script to run, the following packages should also be launched:

    >>> import json
    >>> import numpy as np
    >>> from matplotlib.figure import SubplotParams
    >>> import matplotlib.pyplot as plt

---

### 2. Data preparation

Streamix supplies measured EMG-data in .json and .csv formats.
At first glance, .json files are less cluttered than .csv files, hence this tutorial focusses on this data type.  
If, for some reason, you absolutely have to work with .csv-data, go ahead and ask ChatGPT, because that's what you're going to do anyways.

---

#### *1<sup>st</sup>* of all

Data needs to be loaded:
```py
with open('emg_trial.json', 'r') as file:
    data = json.load(file)
```
#### *2<sup>nd</sup>* of all

For pyemgpipeline to work, the data needs to be stored in a 2d ndarray with shape (n_samples, n_channels), where each column represents data of one channel. 

The following function can be used to extract data from the .json file and store it in a 2d ndarray with the desired shape.

```py
def extract_channel_data_from_json(data):
```
&rarr; The complete version of the function can be found in the exemplary python file for [*pyemgpipeline*](emg_processing.py).

#### *3<sup>rd</sup>* of all

Plot parameters
```py
emg_plot_params = pep.plots.EMGPlotParams()
```

#### *4<sup>th</sup>* of all

Set up information

```py
sample_rate = 500  # Adjust accordingly to respective data
trial_names = ['Trial 1']  # Adjust to fit experiment 
```

#### *Last* of all

Create the EMGMeasurementCollection

```py
c = pep.wrappers.EMGMeasurementCollection(all_data_list, hz=sample_rate, trial_names=trial_names,              channel_names=channel_names, emg_plot_params=emg_plot_params)
```
---


### 3. Data processing

The following steps all adhere to the same structure:
1. The syntax for the code in python is supplied
2. An explanation, what the code does
3. An explanation, why it is reasonable to do so 


For more in-depth studies, points 2. and 3. might be interesting, for the realisation of *pyemgpipeline* only point 1. is relevant.

#### Step 1: DC offset removal
---

1. Python Code
```py
c.apply_dc_offset_remover()
```

2. What it does:

*DC offset* stands for *Direct Current offset*. It represents a constant voltage component in the signal that shifts the baseline of the signal away from zero, creating an unwanted component. Baseline drifts can occur for variuos reasons such as changes in the electrode-skin impedence (due to movements, sweat, etc.) or temperature and humidity fluctuations caused by the environment. These drifts can make it difficult to accurately analyze the signal, hence the removal of the DC offset.
  
3. Why it's reasonable:

Improves Signal Centering: By removing the offset, the signal is centered around zero, making it more accurate for visual inspection and signal processing.
Prepares for Filtering: High-pass and bandpass filters work more effectively when the signal is already centered, as they are designed to remove specific frequency components without being distorted by a non-zero baseline.
Reduces Artifacts in Analysis: The presence of a baseline drift can interfere with the detection of true muscle activity and may cause misinterpretation of the signal during amplitude-based or frequency-domain analyses.



#### Step 2: Bandpass filtering.

1. Python Code
```py
c.apply_bandpass_filter(bf_order=4, bf_cutoff_fq_lo=10, bf_cutoff_fq_hi=200)
```
---
   
2. What it does:

This operation applies a bandpass filter with a 4th-order filter to the signal, only allowing frequencies between 10 Hz and 200 Hz to pass through.  
*The frequencies can and should be adjusted accordingly to the needs of each individual experiment.*

3. Why it's reasonable:

EMG signals typically contain useful information within the range of 10 Hz to 450 Hz. Frequencies outside this range are likely to be noise or irrelevant low-frequency artifacts. Bandpass filtering helps isolate the frequency range that contains meaningful muscle activation data.


#### Step 3: Full wave rectification

1. Python Code
```py
c.apply_full_wave_rectifier()
```
---

2. What it does:

This step takes the absolute value of the EMG signal, converting all negative values to positive ones, effectively rectifying the signal.

3. Why it's reasonable:

The rectified signal is easier to analyze because it highlights the amplitude of muscle activations without the cancellation effect of negative values. This step is crucial for computing the envelope or average of the signal in later stages.

#### Step 4: Linear envelope

1. Python Code

```py
c.apply_linear_envelope(le_order=4, le_cutoff_fq=6)
```
---

2. What it does:

This operation applies a moving average filter with a specified order and a low cutoff frequency to smooth the rectified signal and create a linear envelope.

1. Why it's reasonable:

The linear envelope represents the general trend of muscle activation over time and is used to analyze muscle contraction levels more intuitively. It smooths out high-frequency fluctuations while preserving the overall shape of the signal, making it easier to identify patterns and events.

#### Step 5: End frame cutting

1. Python Code
```py
c.apply_end_frame_cutter(n_end_frames=30)
```

2. What it does:

This step removes a specified number of frames from the end of the trial.

3. Why it's reasonable:

The end of EMG recordings can sometimes contain unwanted artifacts or noise due to stopping procedures, electrode adjustments, or other extraneous factors. Cutting these frames ensures the processed signal remains clean and artifact-free.

#### Step 6: Amplitude normalization 
*Detecting Maximum Amplitude and Normalizing the Signals*
1. Python Code
```py
max_amplitude = c.find_max_amplitude_of_each_channel_across_trials()
c.apply_amplitude_normalizer(max_amplitude)
```

2. What it does

First, the maximum amplitude of the signal in each channel across all trials is detected. Then, the signal amplitude is normalized based on this maximum value.

3. Why it's reasonable: 

Detecting the maximum amplitude provides a reference for the highest signal strength across trials, which is useful for normalization. By normalizing the signal to this reference, all signals are scaled to a consistent range, often between 0 and 1. This allows for easier comparison of signals across different trials, channels, and subjects, as it eliminates variability due to differences in signal strength or electrode placement.

#### Step 7: Segmentation
*This is only relevant, when only a certain data-excerpt is of interest*.
1. Python Code
```py
all_beg_ts = [start_times]  # List of start times for each segment
all_end_ts = [end_times]    # List of end times for each segment
c.apply_segmenter(all_beg_ts, all_end_ts)
```

2. What it does

This step segments the EMG data into smaller portions, defined by the provided start and end times for each segment.

3. Why it's reasonable

Segmenting the data is useful when you want to focus on specific periods of interest, such as muscle activations during particular phases of a task. By specifying the start and end times, you can isolate relevant portions of the signal, making the analysis more focused and manageable. This step helps in extracting meaningful events or phases from the signal while excluding irrelevant or noisy portions.

--- 
  
### 4. Plot and save data

Finally, in a last step, the processed data can be visualised via the c.plot() function.  
Saving the plot as a .jpeg might also come in handy, if the desired outcome is to make the processed data easily accessible and to work with it beyond exercising how to manoeuvre python-packages. 

```py
c.plot()
plt.savefig()
```

--- 

### Theory to practice

The aim of this tutorial is ["to explain step by step how pyemgpipeline can be applied to process EMG-data captured via Streamix (smx)."](##abstract)  
As there is not better test for a tutorial than using it to transfer theoretical knowledge into practice, this document now should be used to complete the following task:

<div style="border: 1px solid #ccc; background-color: #f9f9f9; padding: 10px; border-radius: 5px; margin-top: 10px; margin-bottom: 20px; color: #333;">
    Load, process, plot and save the EMG-data stored in the file <a href="EMG Processing/emg_trial.json">emg_trial</a> by implementing the steps portrayed in this document.<br>
    <i>Hint:</i> it might be a good idea to write your code in the <a href="emg_processing.py">supplied document</a>, because there you can also find the function that can be used to extract data from the .json file and store it in a 2d ndarray with the desired shape.  
    Furthermore, numbers in functions within this tutorial are adapted to the needs of the example. Hence, adjustments to fit particular needs or requirements are not necessary (and neither is a segmentation step).
</div>

<p style="margin-top: 20px;"> <b>CAVE:</b> This data is the test-output from the first trial with the new MyonEMG to Streamix hardware. If the output in the end looks strange, chances are that it is neither your nor the tutorial's fault but rather due to some people randomly tapping on the electrodes.</p>
