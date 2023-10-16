# Vowel-Like-Regions-using-Excitation-Source-Information
Detection of Vowel Like Regions in Speech Signal using excitation source information of the signal. The Detected Regions can be used to extract features for speech classification with the help of Machine Learning and Deep Learning.

# Inference for a single File:
- Navigate to the VOP_plot.ipynb notebook and enter the path of audio file.
- Run all the cells to produce plots for manifesting Vowel Onset Points and Vowel End Points within the speech waveform.

# Developing Classifier Models:
- Extract the Features from Vowel Like Regions by framing the region between Vowel onset Point and it's consecutive Vowel End Point.
- Compute Features like Mel Spectrograms, Formant Frequencies, Average Vowel Usage, Distance Between Consectuive Vowel Usage.
- Extract Features for the Speech Signal Dataset for the Possible Classes and train Classification Models/Neural Networks for Speech Classification.
