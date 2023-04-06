Readme.md for Programming and Scripting Project  
Author: Phelim Barry  


Python v3.10.7   
VS Code: 1.74.3

---

**Table of Contents**
1. [Introduction](#1-Introduction) 
2. [Background](#2-Background)
3. [Methods](#3-Methods)
4. [Results](#4-Results)
    1. res1
    2. res2
    3. res3
    4. etc.
5. [References](#5-References)


# 1. Introduction
The purpose of this project is to research the iris data set and write code (and documentation) in Python to analyse it. 
The iris data set is available to download from http://archive.ics.uci.edu/ml/datasets/Iris 

# 2. Background
The iris data set consists of data published by R. A. Fisher in 1936. It is made up of 150 samples (50 each) of three different types of iris flower - Iris Setosa, Iris Virginica and Iris Versicolor. Each flower was measured for Sepal Length, Sepal Width, Petal Length and Petal Width. 
Although initially used by Fisher to apply his linear discriminant analysis, the data set is widely used today as a beginners learning tool in the areas of machine learning and data analysis.
https://en.wikipedia.org/wiki/Iris_flower_data_set


# 3. Methods
An online search will reveal that the iris data set is very popular and has been researhed and investigated by many in the past. The most popular analysis techniques involve using histograms to plot the individual attributes and using scatter plots to compare pairs of attributes. Basic descriptive statistics are also useful to present a summary of each attribute.
Good link here - https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/   

My approach was to initially write simple code to perform the analysis which meant a lot of duplicate code which although completed the task, wasn't very clean or efficient. 
Once all the code was wroking I then set about cleaning it up and removing duplicates where possible through the use of functions etc.

To perform our analysis we firstly need to import a number of python modules. We import the pandas module for data manimpulation and analysis, the numpy module for arrays and matrices and finally the matplotlib module for plotting data.   

The iris data set is a two dimension array so in order to work with it with import it as a csv file using the pandas read_csv() function.

For our analysis we will start with presenting basic descriptive statistics such as min, max, mean and standard deviation of each attribute. Using the inbuilt python function describe() we could quickly get a full set of summary statistics however this will also include some data not necessary needed for our analysis. So we instead specify the exact statistics we want using the index vaules of the data set by specifying them using .loc[].
https://www.statology.org/pandas-describe-only-mean-std/
https://stackoverflow.com/questions/19124148/modify-output-from-python-pandas-describe



# 4. Results
The results are broken down and displayed in Histograms etc...

# 5. References
Links actually used in the code
http://archive.ics.uci.edu/ml/datasets/Iris - iris data set repository   
https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas - for adding column names to the data sheet   
https://www.statology.org/pandas-describe-only-mean-std/ - using the describe() function   
https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o - help with scatterplots using the plt.clf() function   
https://stackoverflow.com/questions/36512890/python-matplotlib-saved-images-getting-overwritten-while-using-for-loop - help with scatterplots   
https://medium.com/@avulurivenkatasaireddyexploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d - plotting suggestions   
https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column - sorting dataframes   




Usefull Links - TBD if to be included
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
Useful link here
https://www.youtube.com/watch?v=vmEHCJofslg&start=1068
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html - some analysis



#Task suggestions
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
1. Outputs a summary of each variable to a single text file, use statistical analysis - mean, max, min etc.
2. Saves a histogram of each variable to png files, and
3. Outputs a scatter plot of each pair of variables.
4. Performs any other analysis you think is appropriate

