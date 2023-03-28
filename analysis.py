# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
#Read the CSV file and add headers
# reading the CSV file and add column names
#From here - https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
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
#https://www.statology.org/pandas-describe-only-mean-std/
summary_stats = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
with open(FILENAME, 'a') as f: #'a' for append
            summary_stats = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
            string1 = f.write(f"Summary of dataset : \n{summary_stats}\n")

#Histogram Code - (need to add this to a function/loop later to loop through each variable)
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
     for_header = f.write("\nHistogram saved as Sepal_Length_Histogram.png\n\n")
plt.show()

#Maybe not needed anymore
unique_class = iris_csv.Class.unique()




#Everything below here is just for testing
'''
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