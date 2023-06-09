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
    1. [Descriptive Statistics](#41-descriptive-statistics)
    2. [Histograms](#42-histograms)
    3. [Scatterplots](#43-scatterplots)
    4. [Heatmaps](#44-heatmaps)
    5. [Correlations](#45-correlations)
5. [List of Plots](#5-list-of-plots)
6. [Summary](#6-summary)
7. [References](#7-References)


# 1. Introduction
The purpose of this project is to research the iris data set and write documentation and code to research it. 
The iris data set is available to download from http://archive.ics.uci.edu/ml/datasets/Iris 

# 2. Background
The iris data set consists of data published by R. A. Fisher in 1936. It is made up of 150 samples (50 each) of three different types of iris flower - Iris Setosa, Iris Virginica and Iris Versicolor. Each flower was measured for Sepal Length, Sepal Width, Petal Length and Petal Width. 
Although initially used by Fisher to apply his linear discriminant analysis, the data set is widely used today as a beginners learning tool in the areas of machine learning and data analysis.
https://en.wikipedia.org/wiki/Iris_flower_data_set


# 3. Methods
An online search will reveal that the iris data set is very popular and has been researched and investigated by many in the past. The most popular analysis techniques involve using histograms to plot the individual attributes and using scatter plots to compare pairs of attributes. Basic descriptive statistics are also useful to present a summary of each attribute.
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/   

My approach was to initially write simple code to perform the analysis which meant a lot of duplicate code which although completed the task, wasn't very clean or efficient. 
Once all the code was working I then set about cleaning it up and removing duplicates where possible through the use of functions etc. For example, we create and call a function ```text_write()``` whenever we want to write data to the text file and call it from various stages within the code with the argument ```data``` through ```text_write(data)```.

To perform our analysis we firstly need to import the following python modules:   
    pandas - module used for data analysis and manipulation of tabular data   
    numpy - module that offers support for working with arrays and matrices and complex mathematical functions   
    matplotlib - module for plotting data and creating graphical representations of data   
    seaborn - module for statistical plotting and data visualisation   

The iris data set is a two dimension array so in order to work with it we import it as a csv file using the pandas```read_csv()```function. During the reading of the file  we assign column names (which were not present in our original data set) for later use during our analysis.

Using the inbuilt functions ```shape``` and ```info()``` we firstly generate basic information about our data set such as the number of rows and columns and also the column names and data types. These details are written to the text file. Typically the ```info()``` function prints back to the terminal but we supress this and write it only to the text file using code sourced from https://stackoverflow.com/questions/39440253/how-to-return-a-string-from-pandas-dataframe-info. This requires importing the io module ```import io``` which is used to manage file related input and output operations.


For our analysis we will start with presenting basic descriptive statistics such as min, max, mean and standard deviation of each attribute. Using the inbuilt python function ```describe()``` we could quickly get a full set of summary statistics however this will also include some data not necessary needed for our analysis. So we instead specify the exact statistics we want using the indexed values of the data set by specifying them using ```.loc[]```.
https://www.statology.org/pandas-describe-only-mean-std/
https://stackoverflow.com/questions/19124148/modify-output-from-python-pandas-describe

Using a while loop we also present similar stats by flower type. Using the ```unique()``` function we extract the three flower types into a new variable ```unique_class``` and use that in a while loop along with the ```describe()``` function to extract the min, max, mean and standard deviation of each flower type and export it to the analysis.txt file.

Following this we move on to generating various plots to graphically describe the data through histograms and scatterplots. 
For the histograms we have four blocks of code - one for each of the attributes: Petal Length, Petal Width, Sepal Length and Sepal Width. The histogram code starts with creating a new list to store the data and populates it using a for loop that runs through the data set pulling out the data for each variable (e.g. Petal Length). The data is then sorted before generating the histogram using the ```sort()``` function. We then add a plot title and x and y labels before generating the plot and saving it to our directory using ```plt.savefig()```. Finally we write a comment to the text file with the plot name for reference. 
Plots for the remaining three attributes (Petal Width, Sepal Length and Sepal Width) are created in a similar manner. But before creating each new plot we call ```plt.clf()``` to clear the previous plot and start fresh each time.

Next we create two scatterplots to compare two sets of attributes - Petal Length/Petal Width and Sepal Length/Sepal Width. The blocks of code for these are quite similar to the histogram blocks of code but we use ```plt.scatter``` as opposed to ```plot.hist``` to generate the plots.
This shows all the data in one easy to read plot but to expand on it we use seaborn to create two new plots and use different colours to differentiate by flower type. We define new variables for the data for each axis and add a title and label as before then plot the data using ```sns.scatterplot``` and pass the arguement ```hue=iris_csv.Class``` to let seaborn assign colours based on the ```Class``` (i.e. flower type). 

The next plot we generate is a histogram comparing the Petal Length - for each flower type. To generate the data for the histogram we experimented with using ```.loc``` to return the required data into three separate lists (as opposed to the method used earlier to generate the individual histograms) with a list for each flower type. Once we have the data, the actual plotting code is similar to the above but plot the three sets of data using ```plt.hist``` for each one. This results in a single plot with three sets of data.

The final plot we generate is a Heatmap using the seaborn module imported earlier. Seeing as we added the ```Class``` to our dataframe we must remove it before we can create the heatmap using ```.drop("Class", axes=1)``` to avoid a float error.
https://stackoverflow.com/questions/8420143/valueerror-could-not-convert-string-to-float-id
We then generate the heatmap using ```sns.heatmap``` and pass the values ```method='pearson'``` to use Pearson's correlation techniques and also specify the colour map to use with ```cmap="YlGnBl"```.
Again, as can be seen in the analysis.py file we need a lot less lines of code to generate this plot using seaborn than we do generating the histograms or scatterplots using matplotlib which show the power of seaborn.

We create a new function ```text_write``` that is used whenever we want to write data to the text file. This function opens the file and writes the data. Using a function like this saves a number of lines of code and simplifies the script. In order to write the data back to the text file we need to convert it to a string type each time and this is completed using ```to_string()```.
https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file   
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html

In order to provide feedback to the user who runs the script, we create a list called ```outputs``` and populate it at various stages of execution with the details of what the script is doing at that point in time. We then print this back to the terminal upon completion of the script as feedback.

Terminal Command:
```
python3 analysis.py
```
Sample Output:
```
Created analysis.txt to show summary data for the iris data set
Writing summary for the combined data set to analysis.txt
Writing summary data for each flower type to analysis.txt
Generating plots and saving to local directory and writing plot names to analysis.txt
Writing Person's Correlation data to analysis.txt
Finished writing to analysis.txt
```

# 4. Results
The results of the analysis are split between basic descriptive statistics of the data set, which are exported out to the analysis.txt file, and various plots of the data using Histograms, Scatterplots and a Heatmap. We also generate and export a correlation table, using Pearson's correlation techniques, to the analysis.txt file.   
The results of the ```shape``` function show us that the data set has 150 rows and 5 columns. And the ```info()``` function tells us that each attribute (Sepal Length, Sepal Width etc.) has 150 values with no null values in any column.   
## 4.1. Descriptive Statistics
Descriptive Statistics are first exported to the analysis.txt file for the entire data set. This gives an overall view of the min, max, mean and standard deviation for the four main data attributes - Petal Length, Petal Width, Sepal Length and Sepal Width.  We can read from the results for example that Sepal Length has a min and max length of 4.3 and 7.9cm respectively. The mean value for Sepal Length is 5.84cm and the standard deviation is 0.83cm. 
Petal Length on the other hand has min and max values of 1 and 6.9cm with a mean of 3.76cm. We can see from the results how such a range gives a standard deviation of 1.76cm.

Although the overall results described above are useful to see statistics on the data set as a whole, we then complement this by generating and exporting the same statistics but split by the three flower types: Iris-setosa, Iris-versicolor and Iris-virginica. 
Reading this data we can easily pick out flower-specific statistics such as seeing that the Iris-virginica has the longest Sepal Length of 7.9cm compared to 5.8cm for the Iris-setosa and 7.0cm for the Iris-versicolour.
Also we can see that the Iris-setosa has the shortest Petal Length at 1cm compared to the Iris-versicolor (3cm) and Iris-virginica (4.5cm).   

## 4.2. Histograms
Using histograms we can plot the distribution of our data and see the frequency distributions. 

Initially we plot a total of four similar histograms, one for each variable - Petal Length, Petal Width, Sepal Length, Sepal Width. A typical histogram would look like a bell curve with the majority of values falling in or around the middle of the plot to show a normal distribution. However in our plots we can see that only the Sepal Width values show a normal distribution with the majority of values falling between 2.5 and 3.5cm. This matches back to the data produced earlier which showed a standard deviation of 0.43cm for Sepal Width meaning that the majority of values are close to the mean.   
The plots for the other three variables all show non symmetrical distribution. In particular if we look at the plot for Petal Length we can see that almost 50 flowers had a value of between 1 and 2cm with the remaining 100 data points showing a more normal distribution.   
Referring back to our summary statistics we can see that the Iris-setosa family has min and max values of 1 and 1.9cm respectively which would explain why the plot looks as it does. The data from the other two flowers tend to show more normal plots with a lot more values appearing around the means of 4.2 and 5.6cm respectively.

To expand on this analysis some more, we lastly generate a histogram plotting Petal Length values for all three flower types on a single plot. As well as showing the power of the plotting functions this also shows at a glance the frequency distribution of each flower type on a single plot. It's very easy to read and see how the three flower types compare against each other.   
From this we can conclude that the Petal Length for the Iris-setosa is a lot smaller than the other two flower types and the values are within a small range of between 1 and 2cm. While the Iris-Versicolor and Iris-Virginia have much similar values and ranges and overlap quite a bit with all values in the range of 3 to 7cm.

## 4.3. Scatterplots
Scatterplots can be used to indicate the relationships between two different variables and for our analysis we create two scatterplots showing the relationship between Petal Length and Petal Width and then the relationship between Sepal Width and Sepal Length. 

We can see a very linear progression of Petal Length and Petal Width indicating that as the Petal Length increases so does Petal Width. This indicates a very strong relationship between the two variables.

However we also see that the Sepal Width and Sepal Length scatterplot is a lot less linear which indicates little or no relationship between the two variables.

To expand on these scatterplots we create two new plots showing the breakdown by flower type. From the Petal analysis we can see that all three flower types follow a linear progression and that the Iris_setosa is by far the smaller flower with all of it's data points clustered in a small area. In contrast, the Iris-virginica is the largest flower, with the Iris-versicolor sitting in the middle however there is some over lap between the two.
The Sepal analysis by flower type again shows the Iris-setosa out on its own but still showing a linear progression. It can be seen that the Iris-setosa has some of the smallest Sepal Lengths but also some of the largest Sepal Widths. The Iris-virginica and Iris-versicolor show a linear progression to a lesser degree and tend to over lap quite a bit. They also tend to have more outliers than the Iris-setosa. 

## 4.4. Heatmaps   
Finally, using the features of Seaborn we plot a heatmap. We use this heatmap to represent the correlation (Pearson's) between the variables Petal Length, Petal Width, Sepal Length and Sepal Width. This shows the strength of the relationships between each variable. The Heatmap is colour coordinated with the darker blue squares showing a strong relationship and the lighter yellow squares showing a weak relationship. 

From the heatmap we can easily pick out which variables have a strong or a weak relationship. For example, we can see that there is a strong positive relationship between Petal Length and Petal Width (.96) meaning that as the Petal Length increases so does the Petal Width. 

However we can also see that there is a very weak negative relationship between Sepal Width and Sepal Length (-.11).

## 4.5. Correlations 
As well as using the Heatmap described above to graphically represent correlations in the data we can also use the inbuilt ```corr()``` function to generate a table showing the same data. From this table (which is exported to the analysis.txt file) we can see the same correlations as in the Heatmap, such as seeing that the relationship between Petal Length and Petal Width is very strong at .96


# 5. List of Plots
| Filename | Description |
| --- | ---|
| Sepal_Length_Histogram.png | Histogram plotting Sepal Lengths |
| Sepal_Width_Histogram.png | Histogram plotting Sepal Widths
| Petal_Length_Histogram.png | Histogram plotting Petal Lengths
| Petal_Width_Histogram.png | Histogram plottoing Petal Widths
| Sepal_Length_Sepal_Width_Scatterplot.png | Scatterplot plotting Sepal Lengths and Sepal Widths
| Petal_Length_Petal_Width_Scatterplot.png | Scatterplot plotting Petal Lengths and Petal Widths
| Petal_Length_Comparison.png | Histogram comparing Petal Lengths 
| Correlation_Heatmap.png | Heatmap plotting correlations
| Petal_Length_Petal_Width_Scatterplot_Seaborn.png | Scatterplot plotting Petal Lengths and Petal Widths by flower type
| Sepal_Length_Sepal_Width_Scatterplot_Seaborn.png | Scatterplot plotting Sepal Lengths and Sepal Widths by flower type

# 6. Summary
Our analysis of the iris data set made use of some of the standard/built-in functionality of Python as well as additional modules that were imported such as numpy, seaborn, pandas and matplotlib. By making use of these features we were able to generate descriptive statistics of the data set as a whole as well as on the individual flower types and do comparisons of the results. This data was all written to the analysis.txt file.   
We also produced many different types of plots to analyse the data. We generate histograms to show the frequency distribution of the data for the four variables. We generate scatterplots to see if the data has linear relationships, or none at all as the data shows in some cases. Finally we generated a heatmap that can be used to find correlations between different variables so show if they have a strong relationship or not.   
Lastly we generated a table for Pearson's correlation and exported it to the analysis.txt file. This shows the same data as the heatmap but just in a different, exportable format.   

# 7. References

http://archive.ics.uci.edu/ml/datasets/Iris - location of iris data set repository   

https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas - details on adding column names to the data sheet during import process   

https://www.statology.org/pandas-describe-only-mean-std/ - how to customise the output of the describe() function   

https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o - help with scatterplots using the plt.clf() function   

https://stackoverflow.com/questions/36512890/python-matplotlib-saved-images-getting-overwritten-while-using-for-loop - help with creating multiple scatterplots   

https://medium.com/@avulurivenkatasaireddyexploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d - plotting suggestions   

https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column - sorting dataframes   

https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file - converting a dataframe to a string (used when writing the summary to the text file)   

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html - converting a dataframe to a string (used when writing the summary to the text file)   

#https://codesolid.com/matplotlib-vs-seaborn/#aioseo-scatter---matplotlib-vs-seaborn - using seaborn to generate scatterplots   

**Other sources used for reference when deciding ways to approach the analysis**

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/

https://www.youtube.com/watch?v=vmEHCJofslg&start=1068

https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 

http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html

**General sources of reference**

https://www.w3schools.com/python/   

https://www.python.org/   
