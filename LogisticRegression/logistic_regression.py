'''
Created on Dec 8, 2014

@author: luchristopher
'''

import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import export_graphviz
import StringIO

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
            
def evaluateLogisticRegression(train_x,train_y,test_x,test_y):
    lr = LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1e30, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None)
    lr.fit(train_x,train_y)

    lr_result = lr.predict(test_x)
    fpr_lr, tpr_lr, thresholds = roc_curve(test_y, lr_result)
    auc = auc(fpr_lr, tpr_lr)	

    plotAUC(test_y,lr_result,'LR')

    return auc
    
