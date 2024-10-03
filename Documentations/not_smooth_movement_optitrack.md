## What to do if the captured movement is not smooth?

There are several possible solutions to improve the captured movement:

1. **Use the capture software Motive**:  
   Switch to the layout mode by selecting "Layout" in the top right corner and then choosing "Edit".  
   Select your data, right-click on it, and choose "Reconstruct, Auto-label, Solve". This method can address minor issues and improve the smoothness.

2. **Edit the data using Python**:  
   Remove the last few frames from the capture, as they may be inaccurate due to partial marker occlusion. Then, fit a curve to the remaining data that best represents the rest of the movement.
