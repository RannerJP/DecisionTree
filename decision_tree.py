#-------------------------------------------------------------------------
# AUTHOR: Jose Pavon
# FILENAME: descision_tree.py
# SPECIFICATION: This program takes in a file called contact_lens.csv and returns a decision tree for the given features
# FOR: CS 4210- Assignment #1
# TIME SPENT: About 4-5 hours for whole homework
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv


db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
for row in db:
  placeholder = []
  for count,item in enumerate(row):
      if count<4:
        if item == "Young" or item == "Myope" or item == "No" or item == "Reduced":
          placeholder.append(1)
        elif item == "Presbyopic" or item == "Hypermetrope" or item == "Yes" or item == "Normal":
          placeholder.append(2)
        else:
          placeholder.append(3)
  X.append(placeholder)

print(X)
#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
for row in db:
  if row[4] == "Yes":
    Y.append(1)
  else:
    Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()