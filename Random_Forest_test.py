import pandas as pd
import math as m
import numpy as np
import time

from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.metrics import roc_auc_score

InputDF = pd.read_csv('Processed4/Input.csv')
Labels = pd.read_csv('Processed4/Labels.csv')

X = InputDF.sort_values(by='VisitId')

IDs = X.VisitId

Labels.drop_duplicates(subset='VisitId',inplace=True,keep='first')
Labels1 = Labels[Labels.VisitId.isin(IDs)] #(2032, 92)

X.drop(labels='VisitId',axis=1,inplace=True) #(2032, 19071)
# X=X.fillna(X.median())

y_list = Labels1.sort_values(by='VisitId')



#### Response 1: Respiratory Failure
y1 = y_list.loc[:,'qvi_RespiratoryFailure']



#### RF
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
   X,y1, test_size=0.2, random_state=0)

score_list = []
auc_list = []
pred_list = []
for i in range(4,11):
   clf = RandomForestClassifier(n_estimators=1000,max_features='sqrt',class_weight="balanced",
                                max_depth=i,min_samples_leaf=2,random_state=823)
   clf = clf.fit(X_train,y_train)
   score = clf.score(X_test,y_test)
   score_list.append(score)
   print "Accuracy with max depth = " + str(i) + " is: {0:.3f}\n".format(score)
   auc = roc_auc_score(y_test,clf.predict_proba(X_test)[:,1])
   auc_list.append(auc)
   print "AUC with max depth = " + str(i) + " is: {0:.3f}\n".format(auc)
   pred = clf.predict(X_test)
   pred_list.append(pred)

#### Best model: max depth = 6, auc = 0.598
clf = RandomForestClassifier(n_estimators=1000,max_features='sqrt',class_weight="balanced",
                                max_depth=6,min_samples_leaf=2,random_state=823)
clf = clf.fit(X_train,y_train)
auc = roc_auc_score(y_test,clf.predict_proba(X_test)[:,1])

