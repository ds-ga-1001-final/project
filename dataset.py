'''
Created on Nov 12, 2014

@author: luchristopher
'''

import sys
import pandas as pd
import numpy as np

class DataSet():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        try:
            f = open(params)
        except:
            print >> sys.stderr, 'file cannot be opened\n'
        self.df = pd.read_csv(params)
        
    def clean(self):
        self.df = self.df.drop('id',axis=1)
        
    def randomSampling(self,samp_size=1):
        if samp_size <= self.df.shape[0]:
            indices = np.random.randint(0,self.df.shape[0],size = samp_size)
        else:
            sys.exit()
        print self.df.ix[indices,:]
        return self.df.ix[indices,:]
        
        