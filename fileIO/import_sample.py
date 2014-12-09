'''
Created on Dec 8, 2014

@author: luchristopher
'''
import pandas as pd

def read_sample(filename):
    raw_df = pd.read_csv(filename)
    return raw_df

