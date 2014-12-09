'''
Created on Nov 12, 2014

@author: luchristopher
'''

from sklearn.cross_validation import train_test_split
def cleanAndSplit(input_df):
    '''
    cleaning:
        1.drop column 'id'
        2.convert 'click' from [0,1] to [-1,1]
    split:
        1.split the input_df set to train and test, this is not necessary if we are working on real data
    '''
    input_df.drop('id',1,inplace=True)  #drop the unique id variable
    input_df['click'] = input_df['click']*2-1
    train_x, test_x, train_y, test_y = train_test_split(input_df.drop('click',1),input_df['click'],test_size=0.2,random_state=42)  #split the train and the test sets from df
#     print train_x,'\n'
#     print train_y,'\n'
    return train_x,train_y,test_x,test_y
