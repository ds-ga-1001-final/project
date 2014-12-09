'''
Created on Nov 12, 2014

@author: luchristopher
'''
from dataset import *


def main():
    filename = '/Users/luchristopher/Downloads/test_rev2.csv'
    dat = DataSet(filename)
    dat.clean()
    samp_data = dat.randomSampling(100)
    

if __name__ == '__main__':
    main()