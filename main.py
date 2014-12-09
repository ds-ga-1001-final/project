from fileIO import *
from DecisionTree import *
from cleandata import *

def main():
    '''
    entrance to all functionalities
    '''
    data = read_sample('/Users/luchristopher/dataset_ctr/samples/sample_train_8090.csv')
    train_x,train_y,test_x,test_y = cleanAndSplit(data)
    
if __name__ == '__main__':
    main()