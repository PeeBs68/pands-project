# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading the CSV file and add column names
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris_csv = pd.read_csv('iris.data', sep= ",", names=col_names, header=None)

#used later
headers1 = col_names[0:4]

#create a list to hold ouput details for ptinting back to the console upon completion
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

output_data = (f"Created {FILENAME} to show summary data")
outputs.append(output_data)

#Using describe() to show summary stats and specifying the attributes to display
data = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
data = data.to_string(header=headers1, index=True)
#Call the text_write function to write the data to the text file
text_write(f"Summary of Dataset: \n {data}\n\n")
output_data = (f"Writing summary for the combined data set to {FILENAME}")
outputs.append(output_data)

#Create individual variables containing data for each flower types
iris_setosa=iris_csv.loc[iris_csv["Class"]=="Iris-setosa"]
iris_virginica=iris_csv.loc[iris_csv["Class"]=="Iris-virginica"]
iris_versicolor=iris_csv.loc[iris_csv["Class"]=="Iris-versicolor"]

#Create a variable to store the unique classes of iris
unique_class = iris_csv.Class.unique()

#Code to gather and print individual stats for each flower type to the output file
flower=0
while flower < 3:
     data = iris_csv.loc[iris_csv["Class"]==unique_class[flower]]
     data = data.describe().loc[['min', 'max', 'mean', 'std']]
     output_data = (f"Writing summary data for {unique_class[flower]} to {FILENAME}")
     outputs.append(output_data)
     text_write(f"Summary Data for {unique_class[flower]}: \n {data}\n\n")
     flower=flower+1

#Histogram Code - (need to add this to a function/loop later to loop through each variable rather than having 4 sets of very like code)
#Add a few blank lies for presentation purposes
#Add a header to the text file
data = "The following plots are created and stored in this same directory\n\n"
text_write(data)

output_data = (f"Generating plots and saving to local directory and writing plot names to {FILENAME}")
outputs.append(output_data)

#Create a list just for Sepal Length
sepal_l = []
for iris in iris_csv['Sepal Length']:
    sepal_l.append(iris)
#Sort the lsit before creating the histogram
sepal_l.sort()
#Add title and labels
plt.title("Sepal Length")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(sepal_l)
#Save the file
plt.savefig("Sepal_Length_Histogram.png")
#Wtite to the text file
data = "\nSepal_Length_Histogram.png saved showing a plot of Sepal Lengths"
text_write(data)

#Create a list just for Sepal Width 
plt.clf()
sepal_w = []
for iris in iris_csv['Sepal Width']:
    sepal_w.append(iris)
sepal_w.sort()
plt.title("Sepal Width")
plt.xlabel("Width")
plt.ylabel("Frequency")
plt.hist(sepal_w)
plt.savefig("Sepal_Width_Histogram.png")
#Wtite to the text file
data = "\nSepal_Width_Histogram.png saved showing a plot of Sepal Widths"
text_write(data)

#Create a list just for Petal Length
plt.clf()
petal_l = []
for iris in iris_csv['Petal Length']:
    petal_l.append(iris)
petal_l.sort()
plt.title("Petal Length")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(petal_l)
plt.savefig("Petal_Length_Histogram.png")
#Wtite to the text file
data = "\nPetal_Length_Histogram.png saved showing a plot of Petal Lengths"
text_write(data)

#Create a list just for Petal Width 
plt.clf()
petal_w = []
for iris in iris_csv['Petal Width']:
    petal_w.append(iris)
petal_w.sort()
plt.title("Petal Width")
plt.xlabel("Width")
plt.ylabel("Frequency")
plt.hist(petal_w)
plt.savefig("Petal_Width_Histogram.png")
#Wtite to the text file
data = "\nPetal_Width_Histogram.png saved showing a plot of Sepal Lengths"
text_write(data)

#Create a scatter plot to compare Sepal Width and Sepal Length
plt.clf()
plt.scatter(iris_csv['Sepal Length'], iris_csv['Sepal Width'], label='Sepal Length | Sepal Width\n')
plt.title('Sepal Length | Sepal Width')
plt.xlabel('Sepal length')
plt.ylabel('Sepal Width')
plt.legend()
plt.savefig("Sepal_Length | Sepal_Width Scatterplot.png")
#Wtite to the text file
data = "\nSepal_Length | Sepal_Width Scatterplot.png saved showing a plot of Sepal Lengths and Sepal Widths\n"
text_write(data)

#For the scatter plot to compare Petal Width and Petal Length
plt.clf()
plt.scatter(iris_csv['Petal Length'], iris_csv['Petal Width'], label='Petal Length | Petal Width\n')
plt.title('Petal Length | Petal Width')
plt.xlabel('Petal length')
plt.ylabel('Petal Width')
plt.legend()
plt.savefig("Petal Length | Petal Width Scatterplot.png")
#Wtite to the text file
data = "Petal Length | Petal Width Scatterplot.png saved showing a plot of Petal Lengths and Petal Widths\n"
text_write(data)

#Split out each flower type into seperate variables and print a sample plot with 3 data elements
plt.clf()
iris_setosa.sort_values("Petal Length")
iris_virginica.sort_values("Petal Length")
iris_versicolor.sort_values("Petal Length")
plt.title("Petal Length Comparison")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(iris_setosa["Petal Length"],label='iris_setosa')
plt.hist(iris_virginica["Petal Length"],label='iris_virginica')
plt.hist(iris_versicolor["Petal Length"],label='iris_versicolor')
plt.legend()
plt.savefig("Petal_Length_Comparison.png")
#Wtite to the text file
data = "Petal_Length_Comparison.png saved showing a plot comparing Petal Lengths for all three flower types\n"
text_write(data)

#Plotting a Heatmap using seaborn to show correlation
#https://practicaldatascience.co.uk/data-science/how-to-calculate-pearson-correlation-in-pandas
#https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/
#https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
#drop the Class column or else you'll get a float error - see below URL
#https://stackoverflow.com/questions/8420143/valueerror-could-not-convert-string-to-float-id
plt.clf()
iris_csv_sns = iris_csv.drop("Class", axis=1)
sns.heatmap(iris_csv_sns.corr(method='pearson'), cmap="YlGnBu", annot=True); 
plt.title("Heatmap - Pearsons Correllation")
plt.savefig("Heatmap.png")
#Wtite to the text file
data = "Heatmap.png saved showing a plot of person's correllation\n\n"
text_write(data)

#Using inbuilt corr() to generate Pearson's correlation table
#https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
p_corr = iris_csv.corr(method='pearson')
#Convert dataframe to string 
data = p_corr.to_string()
text_write(f"Pearson's Correlation of Dataset: \n {data}\n\n")
output_data = (f"Writing Person's Correlation data to {FILENAME}")
outputs.append(output_data)

output_data = (f"Finished writing to {FILENAME}")
outputs.append(output_data)

#Print the output list which informs the user what the script has done
for output in outputs:
     print (output)


'''Things to do
1 Look into using a list/dict for the plot attributes (titles, labels etc and could use a 
loop/function maybe rather than 4 blocks of identical code)

2 Clean up the output to the txt file for the plots so it reads better
'''
