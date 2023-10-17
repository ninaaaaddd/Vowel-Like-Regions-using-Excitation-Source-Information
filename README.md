# Vowel-Like-Regions-using-Excitation-Source-Information
- Detection of Vowel Like Regions in Speech Signal using excitation source information of the signal. The Detected Regions can be used to extract features for speech classification with the help of Machine Learning and Deep Learning.
- Excitation Source Information from the Speech Signal is extracted with the help of Hilbert Envelope of Linear Prediction Residual of Speech Signal and the Zero Frequency Filtered Output of the Speech Signal.
- First Order Gaussian Differential Operator is used to produce Vowel Onset Point and Vowel End Point Evidence Plots where the Peaks in the plot indicate the Onset and Offset Points at the corresponding time stamps.
  

# Inference for a single File:
- Navigate to the VOP_plot.ipynb notebook and enter the path of audio file.
- Run all the cells to produce plots for manifesting Vowel Onset Points and Vowel End Points within the speech waveform.

# Developing Classifier Models:
- Extract the Features from Vowel Like Regions by framing the region between Vowel onset Point and it's consecutive Vowel End Point.
- Compute Features like Mel Spectrograms, Formant Frequencies, Average Vowel Usage, Distance Between Consectuive Vowel Usage.
- Extract Features for the Speech Signal Dataset for the Possible Classes and train Classification Models/Neural Networks for Speech Classification.
