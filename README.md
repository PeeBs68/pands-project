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
    1. [Descriptive Stats](#41-descriptive-statistics)
    2. [Histograms](#42-histograms)
    3. [Scatterplots](#43-scatterplots)
    4. [Heatmaps](#44-heatmaps)
    5. [Correlations](#45-correlations)
5. [References](#5-References)


# 1. Introduction
The purpose of this project is to research the iris data set and write code (and documentation) in Python to analyse it. 
The iris data set is available to download from http://archive.ics.uci.edu/ml/datasets/Iris 

# 2. Background
The iris data set consists of data published by R. A. Fisher in 1936. It is made up of 150 samples (50 each) of three different types of iris flower - Iris Setosa, Iris Virginica and Iris Versicolor. Each flower was measured for Sepal Length, Sepal Width, Petal Length and Petal Width. 
Although initially used by Fisher to apply his linear discriminant analysis, the data set is widely used today as a beginners learning tool in the areas of machine learning and data analysis.
https://en.wikipedia.org/wiki/Iris_flower_data_set


# 3. Methods
An online search will reveal that the iris data set is very popular and has been researched and investigated by many in the past. The most popular analysis techniques involve using histograms to plot the individual attributes and using scatter plots to compare pairs of attributes. Basic descriptive statistics are also useful to present a summary of each attribute.
Good link here - https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/   

My approach was to initially write simple code to perform the analysis which meant a lot of duplicate code which although completed the task, wasn't very clean or efficient. 
Once all the code was working I then set about cleaning it up and removing duplicates where possible through the use of functions etc.

To perform our analysis we firstly need to import the following python modules:   
    pandas - module used for data analysis and manipulation of tabular data   
    numpy - module that offers support for working with arrays and matrices and complex mathematical functions   
    matplotlib - module for plotting data and creating graphical representations of data   
    seaborn - module for statistical plotting and data visualisation   

The iris data set is a two dimension array so in order to work with it with import it as a csv file using the pandas ```read_csv()``` function. During the reading of the file  we assign column names (which were not present in our original data set) for later use during our analysis.

Using the inbuilt functions shape and info() we firstly generate basic information about our data set such as the number of rows and columns and also the column names and data types. These details are written to the text file. Typically the info() function prints back to the terminal but we supress this and write it only to the text file using code sourced from https://stackoverflow.com/questions/39440253/how-to-return-a-string-from-pandas-dataframe-info


For our analysis we will start with presenting basic descriptive statistics such as min, max, mean and standard deviation of each attribute. Using the inbuilt python function describe() we could quickly get a full set of summary statistics however this will also include some data not necessary needed for our analysis. So we instead specify the exact statistics we want using the index vaules of the data set by specifying them using .loc[].
https://www.statology.org/pandas-describe-only-mean-std/
https://stackoverflow.com/questions/19124148/modify-output-from-python-pandas-describe

Using a while loop we also present similar stats by flower type ... although we know there are 3 flower types we still use the count to get it and to be used oin our loop...

We create a new function 'text_write' that is used whenever we want to write data to the text file. This function opens the file and writes the data. Using a function like this saves a number of lines of code and simplifies the script.
https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file - converting a dataframe to a string (used when writing the summary to the text file)   
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html - (used when writing the summary to the text file) 

In order to provide feedback to the user who runs the script, we create a list and populate it at various stages of execution with the details of what the script is doing. We then print this to the terminal upon completion of the script.

Terminal Command:
```
python3 analysis.py
```
Sample Output:
```
Created analysis.txt to show summary data
Writing summary for the combined data set to analysis.txt
Writing summary data for Iris-setosa to analysis.txt
Writing summary data for Iris-versicolor to analysis.txt
Writing summary data for Iris-virginica to analysis.txt
Generating plots and saving to local directory and writing plot names to analysis.txt
Finished writing to analysis.txt
```

# 4. Results
The results of the analysis are split between basic descriptive statistics of the data set, which are exported out to the analysis.txt file, and various plots of the data...
## 4.1. Descriptive Statistics
Descriptive Statistics are first exported to the analysis.txt file for the entire data set. This gives an overall view of the min, max, mean and standard deviation for the four main data elements - Petal Length, Petal Width, Sepal Length and Sepal Width.   

We then complement this be exporting the same statistics but split by the three flower types - Iris-setosa, Iris-versicolor and Iris-virginica. Reading this data we can easily pick out data such as seeing that the Iris-virginica has the longer Sepal Length of 7.9cm or that the Iris-setosa has the shortest Petal Length at 1cm compared to the Iris-versicolor (3cm) and Iris-virginica (4.5cm).   

## 4.2. Histograms
Using histograms we can plot the distribution of our data and see the frequency distributions. 

We plot a total of four histograms - one for each category. A typical histogram would look like a bell curve with the majprity of values falling in or around the middle of the plot to show a normal distribution. However in our plots we can see that only the Sepal Width values show a normal distribution with the other three categories showing non symmetrical dstribution.

Lastly we generate a histogram plotting Petal Length values for all three flower types on a single plot. As well as showing the power of the plotting functions this also shows at a glance the frequency distribution of each flower type on a single plot. It's very easy to read and see how the three flower types compare against each other. From this we can conclude that the Petal Length for the Iris-Setosa is a lot smaller than the other two flower types and the values are within a small range of between 1 and 2cm. While the Iris-Versicolor and Iris-Virginia have much similar values and ranges and overlap quite a bit.

## 4.3. Scatterplots
Scatterplots can be used to indicate the relationships between two different variables and for our analysis we create two scatterplots showing the relationship between Petal Length and Petal Width and then the relationahip between Sepal Width and Sepal Length. 

We can see a very linear progression of Petal Length and Petal Width indicating that as the Petal Length increases so does Petal Length. This indicates a very strong relationship between the two.

However we also see that the Sepal Width and Sepal Length scatterplot is a lot less linear which indicates little or no relationship between the two.

## 4.4. Heatmaps   
Finally, using the features of Seaborn we plot a heatmap. We use this heatmap to represent the correlation (Pearson's) between the variables Petal Length, Petal Width, Sepal Length and Sepal Width. This shows the strength of the relationships between each variable. The Heatmap is colour coordinated with the darker blue squares whosing a stronge relationship and the lighter yellow squares showing a weak relationship. 

From the heatmap we can easily pick out which variables have a strong or a weak relationship. For example, we can see that there is a strong positive relationship between Petal Length and Petal Width (.96) meaning that as the Petal Length increases so does the Petal Width. 

However we can also see that there is a very weak negative relationship between Sepal Width and Sepal Length (-.11) indicating that as one variable increases the other tends to decrease.

## 4.5. Correlations 
As well as using the Heatmap described above to graphically represent correlations in the data we can also use the inbuilt corr() function to generate a table showing the same data. From this table (which is exported to the analysis.txt file) we can see the same correlations as in the Heatmap, such as seeing that the relationship between Petal Length and Petal Width is very strong at .96

# 5. References
Links actually used in the code
http://archive.ics.uci.edu/ml/datasets/Iris - iris data set repository   
https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas - for adding column names to the data sheet   
https://www.statology.org/pandas-describe-only-mean-std/ - using the describe() function   
https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o - help with scatterplots using the plt.clf() function   
https://stackoverflow.com/questions/36512890/python-matplotlib-saved-images-getting-overwritten-while-using-for-loop - help with scatterplots   
https://medium.com/@avulurivenkatasaireddyexploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d - plotting suggestions   
https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column - sorting dataframes   
https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file - converting a dataframe to a string (used when writing the summary to the text file)   
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html - (used when writing the summary to the text file)   



Usefull Links - TBD if to be included
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
Useful link here
https://www.youtube.com/watch?v=vmEHCJofslg&start=1068
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html - some analysis


