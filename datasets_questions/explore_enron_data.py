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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

max = 0
min = 98522
for x in enron_data:
	print x + " " + str(enron_data[x]['director_fees'])
	if enron_data[x]["exercised_stock_options"] != 'NaN' and enron_data[x]["exercised_stock_options"] > max:
		max = enron_data[x]["exercised_stock_options"]
	if enron_data[x]["exercised_stock_options"] < min:
		min = enron_data[x]["exercised_stock_options"]
print max
print min

