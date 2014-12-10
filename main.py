from fileIO import *
from DecisionTree import *
from dtclean.cleandata import *
from DecisionTree.decision_tree import evaluateDecisionTree
from dtclean import *

def main():
    '''
    entrance to all functionalities
    '''
    data = read_sample('/Users/luchristopher/dataset_ctr/samples/sample_train_80900.csv')
    train_x,train_y,test_x,test_y = cleanAndSplitOneHot(data) #clean and split the dataset to train and test
    print train_x,'\n'
    print type(train_x)
    evaluateDecisionTree(train_x,train_y,test_x,test_y)
    
    
if __name__ == '__main__':
    main()