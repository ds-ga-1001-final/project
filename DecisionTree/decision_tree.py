'''
Created on Dec 8, 2014

@author: luchristopher
'''

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import StringIO, pydot

from sklearn.metrics import roc_auc_score,roc_curve,auc

def plotAUC(truth,pred,lab):
    '''
    plotting roc_auc curves
    '''
    fpr,tpr,thresholds = roc_curve(truth,pred)
    roc_auc = auc(fpr,tpr)
    print 'auc score:\n',roc_auc
#     c = (np.random.rand(),np.random.rand(),np.random.rand())
    plt.plot(fpr,tpr)
    plt.plot([0,1],[0,1],'k--')
    plt.xlim([0.,1.])
    plt.ylim([0.,1.])
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    plt.title('ROC')
    plt.legend(loc='best')
    plt.show()
            
def evaluateDecisionTree(train_x,train_y,test_x,test_y):
    clf = DecisionTreeClassifier(criterion='entropy',min_samples_leaf=1,max_depth=3)
    clf.fit(train_x,train_y)
    p = clf.predict_proba(test_x)[:,1]
    auc = roc_auc_score(test_y,p)
    plotAUC(test_y,clf.predict_proba(test_x)[:,1],'DT')
    return auc
    
def runDecisionTree():
    pass