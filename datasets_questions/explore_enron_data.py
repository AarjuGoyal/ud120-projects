#!/usr/bin/python
# -*- coding: utf-8 -*-

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
import operator
import math


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
#this prints the number of entries in the enron dataset

array_enron_data = []
#print enron_data
features_dict = {}

#with print, all the names will be printed
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


#count is the no. of POI's in the dataset
#ngle_data
'''
i = 0
count = 0
for i in range(0,146):
     single_data = enron_data[array_enron_data[i]]
     if single_data["poi"] == 1:
          count = count + 1

print "No. of POI's",count
'''

count_feature = 0
#this loop prints all the features for a person it can be counted and print, prints the feature
for feature in enron_data[array_enron_data[1]]:
     count_feature = count_feature + 1
     #print feature
print "number of features are ",count_feature


#this will load the poi_names.txt file and count the number of entries
'''poi_enron_data = open('/Users/aarjugoyal/Documents/UD120/ud120-projects/final_project/poi_names.txt','r')
poi_enron_dataset_array = poi_enron_data.readlines()
print "length of POI's is ",len(poi_enron_dataset_array)
'''

#To print all the names of poi_names.txt file
'''for row in poi_enron_dataset_array:
     print row'''

#To find a name James Prentice
'''
flag = 0
for row in poi_enron_dataset_array:
     if row is "Prentice, James":
          print "Found the person"
          flag = 1
          break
if flag == 0:
     print "person not found"
'''

#What is the total value of the stock belonging to James Prentice?
'''
stock_James = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "The total stock of James Prentice is ",stock_James
'''

#The total number of emails from wesley colwell to poi
'''
mail_from_wesley = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "total mails from welsey colwell to POI is ",mail_from_wesley
'''
#What’s the value of stock options exercised by Jeffrey K Skilling?
'''
stock_opt_Jeffrey = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Total stock options by Jeffrey K Skilling",stock_opt_Jeffrey
'''

#calculating the total income of Skilling, Lay and Fastow to know who took the most money
#calculated by the feature total_payments
'''
total_Jeffrey = enron_data["SKILLING JEFFREY K"]["total_payments"]
total_Lay = enron_data["LAY KENNETH L"]["total_payments"]
total_Andrew = enron_data["FASTOW ANDREW S"]["total_payments"]

print total_Jeffrey, total_Lay, total_Andrew

income = { 'SKILLING JEFFREY K':total_Jeffrey, 'KENNETH LAY':total_Lay, 'total_Andrew':total_Andrew}
person_max_money = max(income.iteritems(), key=operator.itemgetter(1))[0]
print "Person with maximum income is ",person_max_money

max_money = max(income.iteritems(), key=operator.itemgetter(1))[1]
print "The maximum take is ",max_money
 '''

#To count the number of people who have quantified salary and email address
'''count_with_salary = 0
count_with_email = 0
for i in range(0,146):
     single_data = enron_data[array_enron_data[i]]
     #print single_data["salary"]
     if single_data["salary"] != "NaN":
          count_with_salary = count_with_salary + 1
     if single_data["email_address"] != "NaN":
         count_with_email = count_with_email + 1
print "People with Quantified salary",count_with_salary
print "People with email address",count_with_email
'''

#What percentage of people in the dataset have “NaN” for their total payments as a whole is this?
'''count_without_total_payments = 0
for i in range(0,146):
     single_data = enron_data[array_enron_data[i]]
     if single_data["total_payments"] == "NaN":
          count_without_total_payments = count_without_total_payments+ 1
print count_without_total_payments
percentage_without_total_payments = float(count_without_total_payments)/len(enron_data)*100

print "Percentage People with NaN in total_payments",percentage_without_total_payments        
'''

#What percentage of POI’s  have “NaN” for their total payments?
'''
count_POI_without_total_payments = 0
for i in range(0,146):
     single_data = enron_data[array_enron_data[i]]
     if single_data["poi"] == "1":
          if single_data["total_payments"] == "NaN":
               count_POI_without_total_payments = count_POI_without_total_payments+ 1
print count_POI_without_total_payments
percentage_POI_without_total_payments = float(count_POI_without_total_payments)/len(enron_data)*100
print "Percentage POI with NaN in total_payments",percentage_POI_without_total_payments        
'''
