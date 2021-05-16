## EHR Data

### Lesson 1: Introduction

1. [Introduction to AI and EHR](https://youtu.be/YKrdjcbsftc)

> EHR: Electronic Medical Record

> HIPAA: Health Insurance Portability and Accountability Accountability Act

2. [Historical Context](https://youtu.be/fZ0J_lTsEwU)
3. [Landscape of EHR Data](https://youtu.be/UOoHQsO-7ww)

> [Google Cloud Healthcare API](https://cloud.google.com/healthcare/docs/concepts/projects-datasets-data-stores)

4. https://youtu.be/BUMBZebewFY
5.
6. https://youtu.be/qRlB7WtRV5Q


### Lesson 2




**High Cardinality**
Cardinality: refers to the number of unique values that a feature has and is relevant to EHR datasets because there are code sets such as diagnosis codes in the order of tens of thousands of unique codes. This only applies to categorical features and the reason this is a problem is that it can increase dimensionality and makes training models much more difficult and time-consuming.

**How do we define a field with high cardinality?**

* Determine if it is a categorical feature.
* Determine if it has a high number of unique values. This can be a bit subjective but we can probably agree that for a field with 2 unique values would not have high cardinality whereas a field like diagnosis codes might have tens of thousands of unique values would have high cardinality.
* Use the `nunique()` method to return the number of unique values for the categorical categories above.
0.

#### TFDV
You are free to use your tool of choice to explore the data and create an EDA report at the end and TFDV currently has some bugs with the latest version of Chrome. The intention of this lesson is to expose you to TFDV as an option to explore your data. While there are other tools for exploratory data analysis, below are some reasons that TFDV can be helpful:
* Interactive and simple descriptive statistics visualization tool  
* Scales to large datasets
    * It uses "Apache Beam's data-parallel processing framework to scale the computation of statistics over large datasets."  
* Can be used to detect anomalies and drift with new data or differences between training and testing splits

Before building a machine learning model, we must first analyze the dataset and assess for common issues that may require preprocessing. We will use the TFDV library to help analyze and visualize the dataset. Some of the information has been adapted from the TFDV page(https://www.tensorflow.org/tfx/data_validation/get_started.

**IMPORTANT** You must use the Chrome browser to see the TFDV library visualizations.

NOTE: Please note that there are other ways we can explore and analyze the data but we will focus on these areas for the course.




1. [EHR Data Security and Analysis Lesson Overview](https://youtu.be/7K2DAQamdtA)
2. [Importance of Data Privacy and Security](https://youtu.be/I1eU3V6u6XU)
3. Key Healthcare Data Security and Privacy Standards https://youtu.be/iIYv5hhBE2o
4.
5. PHI Data Solution https://youtu.be/qWIjLp7Vj8U
6. Importance of EDA https://youtu.be/QFFYldALaCI
7. Dataset Schema Analysis https://youtu.be/hksgY-J4lWM
8.
9.
10. [Analysing the Dataset for High Cardinality](https://youtu.be/g2wPikiYyuM)
11.
