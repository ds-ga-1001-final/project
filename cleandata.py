'''
Created on Nov 12, 2014

@author: luchristopher
'''
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

def cleanAndSplit(input_df):
    '''
    cleaning:
        1.drop column 'id'
        2.convert 'click' from [0,1] to [-1,1]
    split:
        1.split the input_df set to train and test, this is not necessary if we are working on real data because they are naturally split
    type conversion:
        1.use oneHot or label encoding to convert the string variables to numerical
    '''
    input_df.drop('id',1,inplace=True)  #drop the unique id variable
    input_df['click'] = input_df['click']*2-1
    #the list of string variables, omitting the categorical variables that can be converted to integers automatically
    str_variable_list = ['site_id','site_domain','site_category','app_id','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type']
    for name in str_variable_list:
        label_encoder = preprocessing.LabelEncoder()
        input_df[name]=label_encoder.fit_transform(input_df[name])
    train_x, test_x, train_y, test_y = train_test_split(input_df.drop('click',1),input_df['click'],test_size=0.2,random_state=42)  #split the train and the test sets from df
    print train_x,'\n'
    print train_y,'\n'
    return train_x,train_y,test_x,test_y
