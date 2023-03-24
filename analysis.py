# analysis.py
# Author: Phelim Barry
# Purpose: For analysis of iris data set

import pandas as pd
 
#Read in the CSV file  and add column headers (might not need them but handy for when testing)
iris_csv = pd.read_csv('iris.data', sep= ",", header=None)
headers =  ["Sepal L", "Sepal W", "Petal L", "Petal W", "Class"]
iris_csv.columns = headers

#Displaying the contents of the CSV file
print(iris_csv)
print(iris_csv.to_string())
print(iris_csv.loc[148])
print(iris_csv.columns)

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

#Create the file to store the results
FILENAME = "analysis.txt"

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
#        string1 = f.write("Some results...\n")