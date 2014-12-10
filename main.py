from fileIO import *
from DecisionTree import *
from cleandata import *
from DecisionTree.decision_tree import evaluateDecisionTree

def main():
    '''
    entrance to all functionalities
    '''
    data = read_sample('/Users/luchristopher/dataset_ctr/samples/sample_train_364000_1d.csv')
    train_x,train_y,test_x,test_y = cleanAndSplit(data) #clean and split the dataset to train and test
    print train_x,'\n'
    print type(train_x)
    evaluateDecisionTree(train_x,train_y,test_x,test_y)
    
    
if __name__ == '__main__':
    main()