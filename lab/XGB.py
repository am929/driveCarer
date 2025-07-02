import os

import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error, accuracy_score
from numpy import loadtxt
import xgboost
import pickle
from sklearn import model_selection, preprocessing
#33: lambda x:int(x == '?') 将第33列?转化为0 ，对应第34列数值-1
# data = np.loadtxt('dermatology.data.txt', delimiter=',',converters={33: lambda x:int(x == '?'), 34: lambda x:int(x)-1} )
# sz=data.shape
# X,Y=data[:,0:33],data[:,34]
from xgboost import XGBClassifier, Booster
from numpy import loadtxt
import xgboost


data = pd.read_excel(r'./data4.xls')
# X = data.drop(columns='Label')
# y = data['Label']
# X = np.array(X)
# Y = np.array(y)
y = data.iloc[:,0]
y = np.array(y)
X = []
Ear = list(data.iloc[:,1])
Mar = list(data.iloc[:,2])
Har = list(data.iloc[:,3])
# ----数据标准化------
for i in range(len(Ear)):
    a = [Ear[i],Mar[i],Har[i]]
    # print(a)
    X.append(a)
minmax_scaler=preprocessing.MinMaxScaler()
X=minmax_scaler.fit_transform(X)
X = np.array(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#加载numpy的数组到DMatrix对象
xg_train = xgb.DMatrix(X_train, label=y_train)
xg_test = xgb.DMatrix( X_test, label=y_test)

#1.训练模型

param = {
    'booster': 'gbtree',
    # 'objective': 'binary:logistic',
    'objective': 'multi:softmax',
    'num_class':3,
    'gamma': 0.1,
    'max_depth': 9,
    'lambda': 1,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'silent': 1,
    'eta': 0.005,
    'seed': 1,
    'nthread': 6,
    'n_estimators': 50,
    # 'alpha':0

}


watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
num_round = 31500
bst = xgb.train(param, xg_train, num_round, watchlist );


# save model to file
pickle.dump(bst, open("./XGBModel/xgb.pickle.dat", "wb"))

# some time later...

# load model from file
loaded_model = pickle.load(open("./XGBModel/xgb.pickle.dat", "rb"))

# make predictions for test data
train_pr = loaded_model.predict(xg_train)
train_pre = [round(value) for value in train_pr]
y_pred = loaded_model.predict(xg_test)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(y_train,train_pre)
print("train_Accuracy: %.2f%%" % (accuracy * 100.0))
accuracy = accuracy_score(y_test, predictions)
print("test_Accuracy: %.2f%%" % (accuracy * 100.0))

print(y_test)
print(predictions)
#
# # data_y = []
pre = loaded_model.predict(xgb.DMatrix(X))
pre_t = [round(value) for value in pre]
# pre_t = train_pre+predictions
# print(len(pre_t))
# print(len(y))
# print(pre_t)
# print(y)
accuracy = accuracy_score(y,pre_t)
print("test_Accuracy: %.2f%%" % (accuracy * 100.0))
data1 = {'LabelPredict': pre_t}
pd.DataFrame(data1).to_excel(os.path.join('D:/ImageSolu/test/LabelPredict.xls'), sheet_name='Sheet1', index=False, engine='openpyxl')


# #模型寻优
# from sklearn.model_selection import GridSearchCV
#
# # parameters = {'max_depth': [1, 3, 5], 'n_estimators': [50, 100, 150], 'learning_rate': [0.01, 0.05, 0.1, 0.2]}
# # model = XGBClassifier()
# # grid_search = GridSearchCV(model, parameters, scoring='roc_auc', cv=5)
# # grid_search.fit(X_train, y_train)
# # print(grid_search.best_params_)

