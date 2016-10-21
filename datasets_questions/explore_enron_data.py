#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import numpy as np
import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
#this prints the number of entries in the enron dataset

array_enron_data = []
#print enron_data
features_dict = {}

for row in enron_data:
     #print row
     array_enron_data.append(row)
#here all the data is stored in form of array from the data set
array_enron_data = np.array(array_enron_data)

'''for X in np.nditer(array_enron_data):
     print X
     for feature in enron_data[X]:
        count = count + 1
     print count'''

i = 0
count = 0
#count is the no. of POI's in the dataset
#ngle_data
for i in range(0,146):
     single_data = enron_data[array_enron_data[i]]
     if single_data["poi"] == 1:
          count = count + 1

print "No. of POI's",count

count_feature = 0
#this loop prints all the features for a person it can be counted
for feature in enron_data[array_enron_data[1]]:
     count_feature = count_feature + 1
print "number of features are ",count_feature


#this will load the poi_names.txt file and count the number of entries
poi_enron_dataset = np.loadtxt('/Users/aarjugoyal/Documents/UD120/ud120-projects/final_project/poi_names.txt')
print "length of POI's",len(poi_enron_dataset)
