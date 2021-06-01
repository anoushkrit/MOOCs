## Part 1: Pulse Rate Approximation 

Part 1: Pulse Rate Algorithm Project Overview
Algorithm Specifications
You must build an algorithm that:

estimates pulse rate from the PPG signal and a 3-axis accelerometer.
assumes pulse rate will be restricted between 40BPM (beats per minute) and 240BPM
produces an estimation confidence. A higher confidence value means that this estimate should be more accurate than an estimate with a lower confidence value.
produces an output at least every 2 seconds.
Success Criteria
Your algorithm performance success criteria are as follows: the mean absolute error at 90% availability must be less than 15 BPM on the test set. Put another way, the best 90% of your estimates--according to your own confidence output-- must have a mean absolute error of less than 15 BPM. The evaluation function is included in the starter code.

Note that you will not have access to the dataset that the unit test will call AggregateErrorMetric on the output of your RunPulseRateAlgorithm on a test dataset that you do not have access to. The result of this call must be less than 15 BPM for your algorithm's performance to pass. The test set should be easier than the training set, so as long as your algorithm is doing reasonably well on the training data set, it should pass this test.

Some Helpful Tips
Remember to bandpass filter all your signals. Use the 40-240BPM range to create your pass band.
Use plt.specgram to visualize your signals in the frequency domain. You can plot your estimates on top of the spectrogram to see where things are going wrong.
When the dominant accelerometer frequency is the same as the PPG, try picking the next strongest PPG frequency if there is another good candidate.
Sometimes the cadence of the arm swing is the same as the heartbeat. So if you can't find another good candidate pulse rate outside of the accelerometer peak, it may be the same as the accelerometer.
One option for a confidence algorithm is to answer the question, "How much energy in the frequency spectrum is concentrated near the pulse rate estimate?" You can answer this by summing the frequency spectrum near the pulse rate estimate and dividing it by the sum of the entire spectrum.
Dataset
You will be using the Troika[1] dataset to build your algorithm. Find the dataset under datasets/troika/training_data. The README in that folder will tell you how to interpret the data. The starter code contains a function to help load these files.

Zhilin Zhang, Zhouyue Pi, Benyuan Liu, ‘‘TROIKA: A General Framework for Heart Rate Monitoring Using Wrist-Type Photoplethysmographic Signals During Intensive Physical Exercise,’’IEEE Trans. on Biomedical Engineering, vol. 62, no. 2, pp. 522-531, February 2015. Link
Getting Started
The starter code includes a few helpful functions. TroikaDataset, AggregateErrorMetric, and Evaluate do not need to be modified.

Use TroikaDataset to retrieve a list of .mat files containing reference and signal data.
Use scipy.io.loadmat to the .mat file into a python object.
The bulk of the code will be in the RunPulseRateAlgorithm function. You can and should break the code out into multiple functions.
RunPulseRateAlgorithm will take in two filenames and return a tuple of two NumPy arrays--per-estimate pulse rate error and confidence values. Note: Remember to write docstrings for all functions that you write (including RunPulseRateAlgorithm)
Finally, run the Evaluate function to call your algorithm on the Troika dataset and compute an aggregate error metric. Hint: While building the algorithm, you may want to inspect the algorithm errors in more detail.
Instructions
Offline Instructions
Clone the project starter repo here.
Open up the pulse_rate_starter.ipynb in a local program (e.g., spyder IDE, Jupyter Notebooks, etc. which you can find more detailed instructions in the Introduction to Wearables Lesson's Developer's Workflow Concept.)
You are ready to begin Part 1 of the Final Project.
Notes: It is good to confirm that the packages scipy is version 1.2.0+. You can do this by opening a new terminal and typing conda list and confirm the versioning is appropriate.

Online Instructions
You should head to the next Concept Pulse Rate Algorithm.
Confirm that the pulse_rate_starter.ipynbis open and you are ready to complete Part 1 of the Final Project.
