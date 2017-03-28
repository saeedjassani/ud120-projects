#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn.model_selection import train_test_split
f_train, f_test, l_train, l_test = train_test_split(features, labels, test_size=0.3, random_state=42)


from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(f_train, l_train)
pred = clf.predict(f_test)
print l_test
print pred
print int( sum(pred) )

from sklearn import metrics
print metrics.precision_score(pred, l_test)
print metrics.recall_score(pred, l_test)
#from sklearn.metrics import accuracy_score
#print accuracy_score(pred, l_test)
#print len(l_test)
