# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading the CSV file and add column names
# Information on how to add column names during the import taken from https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris_csv = pd.read_csv('iris.data', sep= ",", names=col_names, header=None)

#Create a list of header names used for the describe function below
#headers1 = col_names[0:4]

#create a list to hold output details for printing back to the console upon completion of the script
outputs = []

#Create the file to store the results
FILENAME = "analysis.txt"

#Function for writing data to the text file
def text_write(data):
     with open(FILENAME, 'a') as f:
         data_to_write = f.write(data)

#Write an intro to the results file
data = "This file shows the output of the analysis performed on the iris data set\n\n"
#Call the text_write function to write the data to the text file
text_write(data)

#Append the current completed action to the outputs list for printing upon script completion
output_data = (f"Created {FILENAME} to show summary data for the iris data set")
outputs.append(output_data)


#Generate some basic information on the data set and write them to the text file
#Rows and Columns
data = iris_csv.shape
text_write(f"The number of Rows, Columns in the data set are: {data}\n\n")

#Column Names and Data Types
#Information on how to supress terminal printing taken from https://stackoverflow.com/questions/39440253/how-to-return-a-string-from-pandas-dataframe-info
import io
buf = io.StringIO()
iris_csv.info(buf=buf)
data = buf.getvalue()
text_write(f"The column names and data types in the data set are: \n\n {data}\n\n")


#Using describe() to show summary stats and specifying the attributes to display
#Information on how to limit what the describe function displays taken from https://www.statology.org/pandas-describe-only-mean-std/ 
data = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
#Convert the data to a str in order to be able to export it
#Information on converting a dataframe to a string taken from https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file 
data = data.to_string(header=col_names[0:4], index=True)
#Call the text_write function to write the data to the text file
text_write(f"Summary of Dataset: \n {data}\n\n")
#Append the current completed action to the outputs list for printing upon script completion
output_data = (f"Writing summary for the combined data set to {FILENAME}")
outputs.append(output_data)

#Create a variable to store the unique classes of iris
#unique_class = iris_csv.Class.unique()

#Code to gather and print individual stats for each flower type to the output file
output_data = (f"Writing summary data for each flower type to {FILENAME}")
outputs.append(output_data)
#Create a variable to store the unique classes of iris
unique_class = iris_csv.Class.unique()
flower=0
while flower < 3:
     data = iris_csv.loc[iris_csv["Class"]==unique_class[flower]]
     data = data.describe().loc[['min', 'max', 'mean', 'std']]
     text_write(f"Summary Data for {unique_class[flower]}: \n {data}\n\n")
     flower=flower+1

#Histogram Code
data = "The following plots are created and stored in this same directory"
text_write(data)
#Append the current completed action to the outputs list for printing upon script completion
output_data = (f"Generating plots and saving to local directory and writing plot names to {FILENAME}")
outputs.append(output_data)

#Create a list just for Sepal Length and generate a histogram
sepal_l = []
for iris in iris_csv['Sepal Length']:
    sepal_l.append(iris)
#Sort the list before creating the histogram
sepal_l.sort()
#Add title and labels
plt.title("Sepal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.hist(sepal_l)
#Save the file
plt.savefig("Sepal_Length_Histogram.png")
#Write to the text file
data = "\n\tSepal_Length_Histogram.png"
text_write(data)

#Create a list just for Sepal Width and generate a histogram
#Clear the previous plot
plt.clf()
sepal_w = []
for iris in iris_csv['Sepal Width']:
    sepal_w.append(iris)
sepal_w.sort()
plt.title("Sepal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.hist(sepal_w)
plt.savefig("Sepal_Width_Histogram.png")
#Write to the text file
data = "\n\tSepal_Width_Histogram.png"
text_write(data)

#Create a list just for Petal Length and generate a histogram
plt.clf()
petal_l = []
for iris in iris_csv['Petal Length']:
    petal_l.append(iris)
petal_l.sort()
plt.title("Petal Length")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
plt.hist(petal_l)
plt.savefig("Petal_Length_Histogram.png")
#Write to the text file
data = "\n\tPetal_Length_Histogram.png"
text_write(data)

#Create a list just for Petal Width and generate a histogram
plt.clf()
petal_w = []
for iris in iris_csv['Petal Width']:
    petal_w.append(iris)
petal_w.sort()
plt.title("Petal Width")
plt.xlabel("Width (cm)")
plt.ylabel("Frequency")
plt.hist(petal_w)
plt.savefig("Petal_Width_Histogram.png")
#Write to the text file
data = "\n\tPetal_Width_Histogram.png"
text_write(data)

#Create a scatter plot to compare Sepal Width and Sepal Length
plt.clf()
plt.scatter(iris_csv['Sepal Length'], iris_csv['Sepal Width'], label='Sepal Length | Sepal Width\n')
plt.title('Sepal Length | Sepal Width')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal Width (cm)')
#plt.legend()
plt.savefig("Sepal_Length_Sepal_Width_Scatterplot.png")
#Write to the text file
data = "\n\tSepal_Length_Sepal_Width_Scatterplot.png"
text_write(data)

#Create a scatter plot to compare Petal Width and Petal Length
plt.clf()
plt.scatter(iris_csv['Petal Length'], iris_csv['Petal Width'], label='Petal Length | Petal Width\n')
plt.title('Petal Length | Petal Width')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal Width (cm)')
#plt.legend()
plt.savefig("Petal_Length_Petal_Width_Scatterplot.png")
#Write to the text file
data = "\n\tPetal_Length_Petal_Width_Scatterplot.png"
text_write(data)

#Create Scatterplots using seaborn with colours for each flower type
#Petal Length and Petal Width comparison
plt.clf()
#Define the data for x and y axis
x_axis = iris_csv['Petal Length']
y_axis = iris_csv['Petal Width']
#Add a title and labels
plt.title("Petal length | Petal Width")
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
#Create and save the plot
sns.scatterplot(x=x_axis, y=y_axis, hue=iris_csv.Class, s=90)
plt.savefig("Petal_Length_Petal_Width_Scatterplot_Seaborn.png")
#Write to the text file
data = "\n\tPetal_Length_Petal_Width_Scatterplot - by flower type.png"
text_write(data)

#Sepal Length and Sepal Width comparison
plt.clf()
#Define the data for x and y axis
x_axis = iris_csv['Sepal Length']
y_axis = iris_csv['Sepal Width']
#Add a title and labels
plt.title("Sepal length | Sepal width")
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
#Create and save the plot
sns.scatterplot(x=x_axis, y=y_axis, hue=iris_csv.Class, s=90)
plt.savefig("Sepal_Length_Sepal_Width_Scatterplot_Seaborn.png")
#Write to the text file
data = "\n\tSepal_Length_Sepal_Width_Scatterplot - by flower type.png"
text_write(data)

#Split out each flower type into seperate variables and print a sample histogram plot with 3 data elements
iris_setosa=iris_csv.loc[iris_csv["Class"]=="Iris-setosa"]
iris_virginica=iris_csv.loc[iris_csv["Class"]=="Iris-virginica"]
iris_versicolor=iris_csv.loc[iris_csv["Class"]=="Iris-versicolor"]
plt.clf()
#Sort the data
iris_setosa.sort_values("Petal Length")
iris_virginica.sort_values("Petal Length")
iris_versicolor.sort_values("Petal Length")
#Add title and labels
plt.title("Petal Length Comparison")
plt.xlabel("Length (cm)")
plt.ylabel("Frequency")
#create the plots
plt.hist(iris_setosa["Petal Length"],label='iris_setosa')
plt.hist(iris_virginica["Petal Length"],label='iris_virginica')
plt.hist(iris_versicolor["Petal Length"],label='iris_versicolor')
plt.legend()
plt.savefig("Petal_Length_Comparison_Histogram.png")
#Write to the text file
data = "\n\tPetal_Length_Comparison_Histogram.png"
text_write(data)

#Plotting a Heatmap using seaborn to show correlations with inspiration taken from the following sources:
#https://practicaldatascience.co.uk/data-science/how-to-calculate-pearson-correlation-in-pandas
#https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/
#https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
plt.clf()
#Inspiration on how to drop the Class column to avoid a float error taken from https://stackoverflow.com/questions/8420143/valueerror-could-not-convert-string-to-float-id
iris_csv_sns = iris_csv.drop("Class", axis=1)
sns.heatmap(iris_csv_sns.corr(method='pearson'), cmap="YlGnBu", annot=True); 
plt.title("Heatmap - Pearsons Correllation")
plt.savefig("Correlation_Heatmap.png")
#Write to the text file
data = "\n\tCorrelation_Heatmap.png\n\n"
text_write(data)

#Correlation Table
#Inspiration on using the inbuilt corr() to generate Pearson's correlation table taken from https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
p_corr = iris_csv.corr(method='pearson')
#Convert dataframe to string 
data = p_corr.to_string()
text_write(f"Pearson's Correlation of Dataset: \n {data}\n\n")
#Append the current completed action to the outputs list for printing upon script completion
output_data = (f"Writing Person's Correlation data to {FILENAME}")
outputs.append(output_data)

#Append the current completed action to the outputs list for printing upon script completion
output_data = (f"Script complete and finished writing to {FILENAME}")
outputs.append(output_data)

#Print the output list which informs the user what the script has done
for output in outputs:
     print (output)


