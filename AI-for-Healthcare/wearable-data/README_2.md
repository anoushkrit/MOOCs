
# Wearable Devices 

[nd320-c4-wearble-data-starter](https://github.com/udacity/nd320-c4-wearable-data-starter)

## Lesson 1 

## Lesson 2

2. Refresher on Signals https://youtu.be/vMk-KIhyCbA

$y(t) = Asin(2 \pi + \phi) + C$

3. Digital Sampling https://youtu.be/v1oWGJjWHso
4. Time Domain Plotting https://youtu.be/GGE6UtMIdGc
Time Domain Plotting https://youtu.be/utE-ELSINcw
5. Time Domain Plotting Continued https://youtu.be/MFNXivoCa7Q
6. Exercise 1: Solution https://youtu.be/r8TUTSiA6vQ
7. Interpolation https://youtu.be/RfltUSOwWvE
11. Exercise 2: Solution https://youtu.be/O49HkDz-DwQ
12. Fourier Transform https://youtu.be/zPLA6IgfQ_4
13. Fourier Transform in Practice https://youtu.be/3IWA8tMxxTA

14. Exercise 3: Solution https://youtu.be/Vyp8TwbOi4E
15. Plotting Signals in Frequency Domain https://youtu.be/Ic-wqdanMh0
16. Exercise 4: Spectrograms 
17. Exercise 4: Solution https://youtu.be/lhfTPWIkn28
18. Harmonics https://youtu.be/byUGEDUj-mE
19. Recap https://youtu.be/8-3_S2weklg
## Lesson 3

3. Accelerometer Deep Dive https://youtu.be/GfdLzQl3POk
4. Exercise 1: Step Cadence
5. Exercise 1: Solution https://youtu.be/iG30q6U0TMM
6. PPG Sensor https://youtu.be/PBrbk7-oPR4
7. Exercise 2: PPG Peaks 
8. Exercise 2: Solution https://youtu.be/V0Gpds9E848
9. PPG SNR 
   1.  Signal Quality Evaluation
   The single most important factor that can make or break any algorithm you build is the underlying quality of the signal. As an algorithms engineer you may have the rare opportunity to influence the design of the hardware that will acquire the signal that will then be the input to your algorithms. Being able to provide actionable quantitative feedback for various hardware prototypes will provide endless returns down the line when you start building algorithms based on that hardware.

   We can see an example of this kind of analysis in this paper where the researchers analyzed the effects of different mediums (water vs. air) and temperature on the PPG signal quality and pulse rate estimation from a smartphone sensor.

   First let’s look at the pulse rate algorithm accuracy.

   Pulse rate estimation accuracy vs. temperature and medium
   Pulse rate accuracy acquired from smartphone PPG signals for varying temperature in dry (red) and underwater (blue) environments.

   Pulse rate accuracy deteriorates at cooler temperatures and is worse underwater compared to in air.

   Using a pulse rate algorithm’s accuracy is a great way to evaluate signal quality, especially if the primary thing you want to do with that signal is estimate pulse rate and if you have the algorithm on hand. However, using an algorithm to estimate signal quality can conflate the algorithm accuracy and its idiosyncrasies with the signal quality. Sometimes you may want to look directly at the signal characteristics themselves. Here, the researchers chose to look at signal amplitude.

   PPG signal amplitude vs. temperature and medium
   Smartphone PPG signal amplitude for varying temperature in dry (red) and underwater (blue) environments.

   Again we observe that we get higher amplitudes in dry and warmer environments. This plot implies that a higher signal amplitude corresponds to higher signal quality. But as we have seen previously, with PPG signals, this is not always the case. Motion artifact and ambient light can cause high amplitude peaks in the signal that definitely do not correspond to signal quality. Optimizing for signal amplitude might mean that you build hardware that is extremely susceptible to motion artifacts.

   In the following exercise you will use a more holistic metric to evaluate PPG signal quality called the signal-to-noise ratio that avoids some of these problems.

   Exercise 3: PPG SNR
   Instructions
   Complete the Offline or Online instructions below.
   Read through the whole .ipynb.
   Complete all the code cells that contain ## Your Code Goes Here.
   Offline
   In the repo which you can access here in the repo /intro-to-sensors/exercises/2-ppg-snr/ you should find the following files:
   3_ppg_snr.ipynb
   exercise3.npz
   Open up the python notebook and associated files in your desired editor.
   Note: Instructions can be found in Introduction to Wearable Data's Concept Developer Workflow for how to set up your local environment.

   Online
   Go to the next concept and the 3_ppg_snr.ipynb should be open and the workspace should already contain the appropriate exercise3.npz file. This one will also contain the ppg_peaks.png file for the instructions in markdown.
10. Exercise 3: PPG SNR
11. Exercise 3: Solution https://youtu.be/gQUNhJk2doc
12. ECG Sensor https://youtu.be/uSJb9ZBDTnU
13. Apple Heart Study- Revisited https://youtu.be/zaFuasewbE8
14. Recap: Introduction to Sensors https://youtu.be/9V-0O8RfVgw

## Lesson 4 

1. Intro to Activity Classification https://youtu.be/dteQl6Nxo0g
2. Data Exploration https://youtu.be/mk5A4cLeyy8
   1. https://youtu.be/fRN3iNPxJI8
3. Exercise 1 Solution https://youtu.be/6eqmSZ0Hwos
4. Feature Extraction https://youtu.be/S02ESJAPztg
   1. https://youtu.be/fveNx3NVGqM
5. Feature Extraction Continued https://youtu.be/JjSgg3MjBpg
   1. https://youtu.be/Ssycf56WjLw
6. Activity Classification https://youtu.be/fZXNoeq1ezg
   1. https://youtu.be/xcE_k8K5wPY
7. Hyperparameter Tuning and Regularization https://youtu.be/nsDnNc9zFSk
8. Cross Validation and Feature Importance https://youtu.be/JoABAPvHXIQ
   1. https://youtu.be/ShE5zyg0l9s
9. Exercise 3: Solution https://youtu.be/fxnUCwPc4s4
10. Activity Classification Recap https://youtu.be/1i5obfDHdio


### Summary
We’ve just done our first modeling task with wearable data. It took a while to get here. We had to learn what an accelerometer was and how it collected information about movement, and we had to learn about signal processing to build the features that we used in our model. We were able to build a pretty successful three-class classifier using a random forest and by doing proper hyperparameter optimization. But this problem is about as easy as it gets.

If you’re looking for a challenge, go to the original dataset and see that it actually has four classes -- running, walking, high-intensity biking, and low-intensity biking. You could try building a classifier that can distinguish between high-intensity and low-intensity biking. You’ll also find a PPG signal in the dataset. That might help you discriminate between these two classes. You might also find that it’s impossible. Maybe there’s not enough information in these sensors to solve this problem, or maybe the dataset wasn’t collected as rigorously as we need. Ultimately, low-resistance and high-resistance is subjective, and the dataset description even notes:

...each participant was free to set the pace of the treadmill and pedal rate on the bike so they were comfortable and also to change these settings or stop the exercise at any time.

More often than not, this is the reality of real-world data science problems.

Outline
Understanding Your Data

[Wrist PPG Dataset](https://physionet.org/content/wrist/1.0.0/)
Data Exploration and Visualization Understanding The Literature
Feature Engineering and Extraction Modeling Performance Evaluation Hyperparameter Optimization
Further Resources
Data Exploration
Wrist PPG Dataset
This is a great blog post by Casie Kozrykov who taught me statistics at Google! In it, she describes the dangers of overfitting your brain when you explore your data. Your dataset is a giant inkblot test.
Check out this StackOverflow discussion on the value of data exploration. From one of the responses:

Two weeks spent training a neuralnet can save you 2 hours looking at the input data

And finally, a blog post from a machine learning practitioner on the data exploration.

Feature Creation
This blog post, [Machine Learning with Signal Processing Techniques](http://ataspinar.com/2018/04/04/machine-learning-with-signal-processing-techniques/), goes through a very similar process as this lesson. It starts by explaining some signal processing techniques (like we did earlier in the course). The author uses those techniques to build features in much the same way we just did. And then, he uses those features to build an activity classification model, just as we are about to!

The algorithm we built was inspired by these two papers.

[Mehrang S., Pietilä J., Korhonen I. An Activity Recognition Framework Deploying the Random Forest Classifier and A Single Optical Heart Rate Monitoring and Triaxial Accelerometer Wrist-Band. Sensors. 2018;18:613. doi: 10.3390/s18020613.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5856093/)

[Liu S, Gao RX, Freedson PS. Computational methods for estimating energy expenditure in human physical activities. Med Sci Sports Exerc. 2012;44:2138–2146. doi: 10.1249/MSS.0b013e31825e825a.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3475744/)

Model Building
Random forests are boosted decision tree models. You need to understand a decision tree before learning what a random forest model is. Start with the sklearn tutorial on decision trees. Then check out these videos on youtube for a visual explanation:

Decision Trees Part 1 Decision Trees Part 2 Random Forest Part 1 Random Forest Part 2

See this list of classification accuracy metrics that can be computed in sklearn.

Follow this series of blog posts for an understanding of how these accuracy metrics work on multiclass problems like ours.

Hyperparameter Optimization
Nested cross-validation can be a tricky concept to wrap your head around. Here are three different explanations from three different authors. Maybe one of the following resources will explain it in a way that clicks for you:

Nested CV - Weina Jin
Nested CV - Elder Research
Nested CV - Stack Exchange: Cross Validated
Our code implementing nested CV was pretty verbose so that you could see all the steps. As with almost everything in ML, sklearn can do it for us as well and you can learn more about Nested CV in sklearn through the documentation.

Is overfitting our hyperparameters really a problem in practice? Yes (or so says this 2010 paper)

An explanation on the difference between hyperparameters and regular parameters with this article from Machine Learning Mastery.

If you want to learn more about Regularization through this article from Towards Data Science.

Glossary
Hyperparameter: A parameter of the model that dictates how the model learns. This is not trained during the training process of the model itself.
Regularization: Regularization is a technique to reduce overfitting of a model by discouraging complexity in the model.
Nested cross-validation: A technique to determine model performance when hyperparameters are also optimized.
Cross-validation: A technique for estimating model performance where multiple models are trained and tested each on a separate partition of the entire dataset.
Classification accuracy: The percent of correct classifications made by a model.



## Lesson 5

1. Introduction to ECG Signal Processing https://youtu.be/7bGv86e09YA
2. Heart Physiology https://youtu.be/BIkZwowLeRc
3. Pan Tompkins Algorithm https://youtu.be/8fb5IJjV-Yo
4. Pan Tompkins Code https://youtu.be/oNFyQT--irs
5. Pan Tompkins Solution https://youtu.be/-OOiZyOWmuU
6. Atrial Fibrillation https://youtu.be/VGi988eAI0I
7. Arrhythmia Detection Dataset https://youtu.be/_E8zA1VDgfM'
   
   https://youtu.be/DbC7fBVwfu4
8. Arrhythmia Detection: Features https://youtu.be/DbC7fBVwfu4
9. Exercise 2: Solution https://youtu.be/Qr4Erwd5mXk
10. Exercise 3: Solution https://youtu.be/07-c7n6WdiM
11. Recap: ECG Signal Processing https://youtu.be/nEg2YpvHNAU
12. Course Recap https://youtu.be/SOnmTveoGhs


