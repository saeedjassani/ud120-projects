#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")
from math import isnan
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',  'expenses', 'exercised_stock_options', 'bonus', 'total_stock_value', 'loan_advances', 'long_term_incentive', 'total_payments', 'fraction_of_deferred_income_to_total_payments']
features_list_1 = ['poi','salary', 'to_messages'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
	
### Task 2: Remove outliers
identified_outliers = ["TOTAL"]
for outlier in identified_outliers:
    data_dict.pop(outlier)

### Task 3: Create new feature(s)
# deferral_payments / total_payments
# from_poi_to_this_person / from_messages
# from_this_person_to_poi / to_messages
for x in data_dict:
    for feature in ['deferred_income',
                    'total_payments'
                   ]:
        if isnan(float(data_dict[x][feature])):
            data_dict[x][feature] = 0

    if data_dict[x]['total_payments'] > 0:
       data_dict[x]['fraction_of_deferred_income_to_total_payments'] = int(data_dict[x]['deferred_income']) / int(data_dict[x]['total_payments'])
    else:
       data_dict[x]['fraction_of_deferred_income_to_total_payments'] = 0

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clfGB = GaussianNB()
from sklearn.svm import SVC
clfSV = SVC(kernel='rbf',C=100)
from sklearn.tree import DecisionTreeClassifier
clfDT= DecisionTreeClassifier()


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clfGB.fit(features_train,labels_train)
predGB=clfGB.predict(features_test)
clfSV.fit(features_train,labels_train)
predSV=clfSV.predict(features_test)
clfDT.fit(features_train,labels_train)
predDT=clfDT.predict(features_test)
from sklearn.metrics import classification_report
target_names = ['Not PoI', 'PoI']
print "GaussianNB"
print( classification_report(labels_test, predGB, target_names=target_names))
print "Support Vector Classifier"
print( classification_report(labels_test, predSV, target_names=target_names))
print "Decision Tree"
print( classification_report(labels_test, predDT, target_names=target_names))
# Example starting point. Try investigating other evaluation techniques!
from sklearn.grid_search import GridSearchCV
param_grid = {'min_samples_split': np.arange(2, 10)}
tree = GridSearchCV(DecisionTreeClassifier(), param_grid)
tree.fit(features_train, labels_train)
print(tree.best_params_)


clf=tree
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)