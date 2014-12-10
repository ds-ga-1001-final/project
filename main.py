from fileIO import *
from DecisionTree import *
from dtclean.cleandata import *
from DecisionTree.decision_tree import evaluateDecisionTree
<<<<<<< HEAD
from dtclean import *
=======
from LogisticRegression.logistic_regression import *
>>>>>>> 57f022c87da9a2f6a2328f63a0c86f5fedc17072

def main():
    '''
    entrance to all functionalities
    '''
    data = read_sample('/Users/luchristopher/dataset_ctr/samples/sample_train_80900.csv')
    train_x,train_y,test_x,test_y = cleanAndSplitOneHot(data) #clean and split the dataset to train and test
    print train_x,'\n'
    print type(train_x)
    evaluateDecisionTree(train_x,train_y,test_x,test_y)
    #evaluateLogisticRegression(train_x,train_y,test_x,test_y)
    
if __name__ == '__main__':
    main()
