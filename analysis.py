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
x=0
while x < 3:
     data = iris_csv.loc[iris_csv["Class"]==unique_class[x]]
     data = data.describe().loc[['min', 'max', 'mean', 'std']]
     output_data = (f"Writing summary data for {unique_class[x]} to {FILENAME}")
     outputs.append(output_data)
     text_write(f"Summary Data for {unique_class[x]}: \n {data}\n\n")
     x=x+1

'''Function to gather and print individual stats for each flower type to the output file
def individual_stats():
    setosa_stats = iris_setosa.describe().loc[['min', 'max', 'mean', 'std']]
    versicolor_stats = iris_versicolor.describe().loc[['min', 'max', 'mean', 'std']]
    virginica_stats = iris_virginica.describe().loc[['min', 'max', 'mean', 'std']]
    with open(FILENAME, 'a') as f:
         string1 = f.write(f"\n\nSummary Data for {unique_class[0]}\n")
         summary1 = f.write(str(setosa_stats))
         string1 = f.write(f"\n\nSummary Data for {unique_class[1]}\n")
         summary2 = f.write(str(versicolor_stats))
         string1 = f.write(f"\n\nSummary Data for {unique_class[2]}\n")
         summary3 = f.write(str(virginica_stats))

#Call the individual_stats function - (maybe can be cleaned up to reduce code later)
individual_stats()'''

#Histogram Code - (need to add this to a function/loop later to loop through each variable rather than having 4 sets of very like code)
#Add a few blank lies for presentation purposes
#Add a header to the text file
data = "The following plots are created and stored in this same directory\n\n"
text_write(data)

output_data = (f"Generating plots and saving to local directory and writing plot names to {FILENAME}")
outputs.append(output_data)

#Create a list just for Sepal Length 
sepal_l = []
for x in iris_csv['Sepal Length']:
    sepal_l.append(x)
sepal_l.sort()
plt.title("Sepal Length")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(sepal_l)
plt.savefig("Sepal_Length_Histogram.png")
data = "\nSepal_Length_Histogram.png saved showing a plot of Sepal Lengths"
text_write(data)

#Create a list just for Sepal Width 
plt.clf()
sepal_w = []
for x in iris_csv['Sepal Width']:
    sepal_w.append(x)
sepal_w.sort()
plt.title("Sepal Width")
plt.xlabel("Width")
plt.ylabel("Frequency")
plt.hist(sepal_w)
plt.savefig("Sepal_Width_Histogram.png")
data = "\nSepal_Width_Histogram.png saved showing a plot of Sepal Widths"
text_write(data)

#Create a list just for Petal Length
plt.clf()
petal_l = []
for x in iris_csv['Petal Length']:
    petal_l.append(x)
petal_l.sort()
plt.title("Petal Length")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(petal_l)
plt.savefig("Petal_Length_Histogram.png")
data = "\nPetal_Length_Histogram.png saved showing a plot of Petal Lengths"
text_write(data)

#Create a list just for Petal Width 
plt.clf()
petal_w = []
for x in iris_csv['Petal Width']:
    petal_w.append(x)
petal_w.sort()
plt.title("Petal Width")
plt.xlabel("Width")
plt.ylabel("Frequency")
plt.hist(petal_w)
plt.savefig("Petal_Width_Histogram.png")
data = "\nPetal_Width_Histogram.png saved showing a plot of Sepal Lengths"
text_write(data)

#For the scatter plot for Sepal Width and Sepal Length
plt.clf()
plt.scatter(iris_csv['Sepal Length'], iris_csv['Sepal Width'], label='Sepal Length | Sepal Width\n')
plt.title('Sepal Length | Sepal Width')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Sepal Width [cm]')
plt.legend()
plt.savefig("Sepal_Length | Sepal_Width Scatterplot.png")
data = "\nSepal_Length | Sepal_Width Scatterplot.png saved showing a plot of Sepal Lengths and Sepal Widths\n"
text_write(data)

#For the scatter plot for Petal Width and Petal Length
plt.clf()
plt.scatter(iris_csv['Petal Length'], iris_csv['Petal Width'], label='Petal Length | Petal Width\n')
plt.title('Petal Length | Petal Width')
plt.xlabel('Petal length [cm]')
plt.ylabel('Petal Width [cm]')
plt.legend()
#plt.show()
plt.savefig("Petal Length | Petal Width Scatterplot.png")
data = "Petal Length | Petal Width Scatterplot.png saved showing a plot of Petal Lengths and Petal Widths\n"
text_write(data)

#To split out each flower type into seperate variables and print a sample plot
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
data = "Petal_Length_Comparison.png saved showing a plot comparing Petal Lengths for all three flower types\n"
text_write(data)

#Heatmap using seaborn
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
data = "Heatmap.png saved showing a plot of person's correllation\n\n"
text_write(data)

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
