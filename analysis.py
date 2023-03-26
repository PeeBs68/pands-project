# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
#Read the CSV file and add headers
iris_csv = pd.read_csv('iris.data', sep= ",", header=None)
headers =  ["Sepal L", "Sepal W", "Petal L", "Petal W", "Class"]
headers1 = headers[0:4]
iris_csv.columns = headers

#Create the file to store the results
FILENAME = "analysis.txt"

#Write an into to the results file
with open(FILENAME, 'a') as f:
     for_header = f.write("This fle shows the output of the analysis performed on the iris data set\n\n")

#Histogram Code - (need to add this to a function/loop later to loop through each variable)
#Create a list just for Sepal Length 
sepal_l = []
for x in iris_csv['Sepal L']:
    sepal_l.append(x)
sepal_l.sort()
plt.title("Sepal Length")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.hist(sepal_l)
plt.savefig("Sepal_Length_Histogram.png")
with open(FILENAME, 'a') as f:
     for_header = f.write("Histogram saved as Sepal_Length_Histogram.png\n\n")
plt.show()

#Uncomment this on Monday
#create a function to gather summary stats on the data set and write to the output file
'''def summary_stats():
     num_rows = len(iris_csv)
     num_cols = len(iris_csv.columns)
     print (num_rows, num_cols)
     with open(FILENAME, 'a') as f:
          for_summary = f.write(f"The iris data set contains {num_rows} rows and {num_cols} columns of data to analyse\n\n")

#call the summary_stats function
summary_stats()'''

#Uncomment this on Wednesday
'''unique_class = iris_csv.Class.unique()

def summary_data(Class):
      #need to loop through each attribute here
      #use headers1 list
      x = 0
      while x < 4:
        print (headers1[x])
        Total = iris_csv[headers1[x]].sum()
        Mean = iris_csv[headers1[x]].mean()
        Max = iris_csv[headers1[x]].max()
        Min = iris_csv[headers1[x]].min()
        x = x+1
        print(f"Min: {Min}")
        return (headers1[x],Total, Mean, Max, Min)

for Class in unique_class:
        print (Class)
        x = 0
        with open(FILENAME, 'a') as f: #'a' for append
            headers1[x],Total, Mean, Max, Min = summary_data(Class)
            string1 = f.write(f"Iris Type : {Class}\n")
            string1 = f.write(f"Attribute : {headers1[x]}, Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}\n")
'''



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