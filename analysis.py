# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading the CSV file and add column names
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris_csv = pd.read_csv('iris.data', sep= ",", names=col_names, header=None)

#used later
headers1 = col_names[0:4]

#Create the file to store the results
FILENAME = "analysis.txt"

#Write an intro to the results file
with open(FILENAME, 'a') as f:
     for_header = f.write("This file shows the output of the analysis performed on the iris data set\n\n")

#Using describe() to show summary stats and specifying what to display
summary_stats = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
with open(FILENAME, 'a') as f: #'a' for append
            summary_stats = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
            string1 = f.write(f"Summary of dataset : \n{summary_stats}\n")

#Histogram Code - (need to add this to a function/loop later to loop through each variable rather than having 4 sets of very like code)
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
with open(FILENAME, 'a') as f:
     for_header = f.write("\nHistogram saved as Sepal_Length_Histogram.png")

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
with open(FILENAME, 'a') as f:
     for_header = f.write("\nHistogram saved as Sepal_Width_Histogram.png")

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
with open(FILENAME, 'a') as f:
     for_header = f.write("\nHistogram saved as Petal_Length_Histogram.png")

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
with open(FILENAME, 'a') as f:
     for_header = f.write("\nHistogram saved as Petal_Width_Histogram.png\n")

#For the scatter plot for Sepal Width and Sepal Length
plt.clf()
plt.scatter(iris_csv['Sepal Length'], iris_csv['Sepal Width'], label='Sepal Length | Sepal Width\n')
plt.title('Sepal Length | Sepal Width')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Sepal Width [cm]')
plt.legend()
plt.savefig("Sepal Length | Sepal Width Scatterplot.png")
with open(FILENAME, 'a') as f:
     for_header = f.write("Scatter Plot saved as Sepal Length | Sepal Width Scatterplot.png\n")

#For the scatter plot for Petal Width and Petal Length
plt.clf()
plt.scatter(iris_csv['Petal Length'], iris_csv['Petal Width'], label='Petal Length | Petal Width\n')
plt.title('Petal Length | Petal Width')
plt.xlabel('Petal length [cm]')
plt.ylabel('Petal Width [cm]')
plt.legend()
#plt.show()
plt.savefig("Petal Length | Petal Width Scatterplot.png")
with open(FILENAME, 'a') as f:
     for_header = f.write("Scatter Plot saved as Petal Length | Petal Width Scatterplot.png\n\n")

#Maybe not needed anymore?
unique_class = iris_csv.Class.unique()

#To split out each flower type into seperate variables and print a sample plot
iris_setosa=iris_csv.loc[iris_csv["Class"]=="Iris-setosa"]
iris_virginica=iris_csv.loc[iris_csv["Class"]=="Iris-virginica"]
iris_versicolor=iris_csv.loc[iris_csv["Class"]=="Iris-versicolor"]
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
plt.savefig("Petal Length Comparison.png")
with open(FILENAME, 'a') as f:
     for_header = f.write("\nHistogram saved as Petal Length Comparison.png")

def write_data():
    xxx = iris_setosa.describe().loc[['min', 'max', 'mean', 'std']]
    yyy = iris_versicolor.describe().loc[['min', 'max', 'mean', 'std']]
    zzz = iris_virginica.describe().loc[['min', 'max', 'mean', 'std']]
    print (unique_class[0])
    print (xxx)
    with open(FILENAME, 'a') as f:
         string0 = f.write(f"\n\nSummary Data for {unique_class[0]}\n")
         string1 = f.write(str(unique_class[0]))
         string2 = f.write(str(xxx))
    print (unique_class[1])
    print (yyy)
    with open(FILENAME, 'a') as f:
         string0 = f.write(f"\n\nSummary Data for {unique_class[1]}\n")
         string1 = f.write(str(unique_class[1]))
         string2 = f.write(str(yyy))
    print (unique_class[2])
    print (zzz)
    with open(FILENAME, 'a') as f:
         string0 = f.write(f"\n\nSummary Data for {unique_class[2]}\n")
         string1 = f.write(str(unique_class[2]))
         string2 = f.write(str(zzz))

write_data()

'''Things to do
1 Add individual stats by flower type

2 Look into using a list/dict for the plot attributes (titles, labels etc and could use a 
loop/function maybe rather than 4 blocks of identical code)

3 Clean up the output to the txt file for the plots so it reads better
'''

#Everything below here is just for testing for now
'''

#Prnting Mean, Max, Min, Sun
#Total = iris_csv['Sepal L'].sum()
#Mean = iris_csv['Sepal L'].mean()

#playing with different print options
for x in iris_csv['Sepal L']:
    print(x)

for x in iris_csv.columns:
    print(iris_csv[x].unique())

#Prnting Mean, Max, Min, Sun
Total = iris_csv['Sepal L'].sum()
Mean = iris_csv['Sepal L'].mean()
Max = iris_csv['Sepal L'].max()
Min = iris_csv['Sepal L'].min()
print(f"Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}")


#Create a function for appending results
def append_results():
     with open(FILENAME, 'a') as f:
          string1 = f.write("Some results...\n")

#stripping data from individual columns
unique_class = str(iris_csv.Class.unique())
class1 = iris_csv.Class[0]
class2 = iris_csv.Class[1]
class3 = iris_csv.Class[2]
print (class1)

print (unique_class)
with open(FILENAME, 'a') as f: #'a' for append
        string1 = f.write(f"Iris Types : {unique_class}\n")
        string1 = f.write(f"Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}")

#Call the functions
#append_results()

#Or do the append normally
#with open(FILENAME, 'a') as f: #'a' for append
#        string1 = f.write("Some results...\n")'''