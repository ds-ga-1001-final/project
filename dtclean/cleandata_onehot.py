'''
Created on Dec 9, 2014

@author: luchristopher
'''
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import decomposition
import numpy as np

# def calculateExplainedVarianceRatio(X_proj,sps_matrix):
#     explained_variances = np.var(X_proj, axis=0) / np.var(sps_matrix, axis=0).sum()
#     return explained_variances

def truncSVD(sps_matrix,components_num):
    tSVD = decomposition.TruncatedSVD(n_components=components_num,random_state=42)  #choose the 20 largest variance contribution components
    truncated_X = tSVD.fit_transform(sps_matrix)
    print 'Total Explained Variance Contribution for {} Components: '.format(components_num),tSVD.explained_variance_ratio_.sum(),'\n'
    return truncated_X
    

def cleanAndSplitOneHot(input_df):
    input_df.drop('id',1,inplace=True)  #drop the unique id variable
    input_df['click'] = input_df['click']*2-1
    Y = input_df['click'].values.reshape(input_df.shape[0],1)   #transpose the Y data to make it n by 1
    X_time = input_df['hour'].values
    X_time = X_time.reshape(X_time.shape[0],1)  #reshape the X_time to make it a n by 1 matrix
    X_df = input_df.drop(['click','hour'],1)
    print Y,X_time
    #the list of string variables, omitting the categorical variables that can be converted to integers automatically
    str_variable_list = ['site_id','site_domain','site_category','app_id','app_domain','app_category','device_id','device_ip','device_model','device_type','device_conn_type']
    for name in str_variable_list:
        label_encoder = preprocessing.LabelEncoder()
        X_df[name]=label_encoder.fit_transform(X_df[name])
    for column in X_df.columns:
        X_df[column] = X_df[column]-min(X_df[column].min(),0) #eliminate negative values for one hot encoding
    X = X_df.values
    print '\n'
    print X
    one_hot_enc = preprocessing.OneHotEncoder()
    one_hot_X = one_hot_enc.fit_transform(X)
    print 'OneHotX:',type(one_hot_X),'\n',one_hot_X,'\n' #one hot sparse matrix generated
    
    #run truncSVD
    truncated_X = truncSVD(one_hot_X,200)   #calculate the truncated SVD matrix with 200 components
    
    #concatenate the truncated principle components with the ordinal datetime variable to generate the train set
    X = np.concatenate((X_time,truncated_X),axis=1)
    print 'Cleaned X set: ',X.shape,'\n'
    print X
    
    #train test split
    train_x, test_x, train_y, test_y = train_test_split(X,Y,test_size=0.2,random_state=42)  #split the train and the test sets from df
    print train_x,'\n'
    print train_y,'\n'
    return train_x,train_y,test_x,test_y