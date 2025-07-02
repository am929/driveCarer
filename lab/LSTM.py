import math
import numpy
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
import  pandas as pd
import  os
from keras.models import Sequential, load_model
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler

dataframe = pd.read_excel(r'./LabelPredict(74%).xls', sheet_name='Sheet1' , usecols=['LabelPredict'], engine='openpyxl', skipfooter=3)
dataset = dataframe.values
# 将整型变为float
dataset = dataset.astype('float32')
# fix random seed for reproducibility
# numpy.random.seed(7)
#归一化,LSTM可以不进行归一化的操作，但是这样会让训练模型的loss下降很慢。
# scaler = MinMaxScaler(feature_range=(0, 1))
# dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.8)
trainlist = dataset[:train_size]
testlist = dataset[train_size:]

def create_dataset(dataset, look_back):
#这里的look_back与timestep相同
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return numpy.array(dataX),numpy.array(dataY)
#look_back=90，根据前90个的数据预测后一个数据的值
look_back = 90
trainX,notTrainY  = create_dataset(trainlist,look_back)
testX,notTestY = create_dataset(testlist,look_back)


#根据正确的标签值来进行训练（就是不根据自己用XGBoost分类预测出来的数据进行模型的检验了）
dataframe = pd.read_excel(r'./data4.xls', sheet_name='Sheet1' , usecols=['Label'], engine='openpyxl', skipfooter=3)
dataset = dataframe.values
# 将整型变为float
dataset = dataset.astype('float32')
#归一化,LSTM可以不进行归一化的操作，但是这样会让训练模型的loss下降很慢。
# scaler = MinMaxScaler(feature_range=(0, 1))
# dataset = scaler.fit_transform(dataset)

train_size = int(len(dataset) * 0.8)
trainlist = dataset[:train_size]
testlist = dataset[train_size:]

look_back = 90
notTrainX,trainY  = create_dataset(trainlist,look_back)
notTestX,testY = create_dataset(testlist,look_back)


trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1] ,1 ))

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(3, input_shape=(90,1)))
# model.add(Dense(1))
model.add(Dense(1, activation='linear'))
# compile model
# model.compile(loss='mse', optimizer='adam')
# model.add(Dropout(0.2))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=70, batch_size=6, shuffle=False, verbose=1)
model.save(os.path.join("DATA","LSTMTest" + ".h5"))
# make predictions
model = load_model(os.path.join("DATA","LSTMTest" + ".h5"))

# print(trainX[0])
# print(testX)
# print(len(testX))
# print(len(testX[0]))

trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
# print(trainPredict)
# print(testPredict)

#反归一化
# trainPredict = scaler.inverse_transform(trainPredict)
# trainY = scaler.inverse_transform(trainY)
# testPredict = scaler.inverse_transform(testPredict)
# testY = scaler.inverse_transform(testY)

# print(trainPredict)
# print(testPredict.astype(int))
# print(len(trainPredict))
# print(len(trainPredict[0]))

# print(trainPredict[0].astype(int))
# print(trainY[0].astype(int))

print ('训练集predicting, classification accuy=%f' % (sum( trainPredict[i].astype(int) == trainY[i] for i in range(len(trainY))) / float(len(trainY)) ))
print ('测试集predicting, classification accuy=%f' % (sum( testPredict[i].astype(int) == testY[i] for i in range(len(testY))) / float(len(testY)) ))

print(trainPredict.astype(int))
print(len(trainPredict[0].astype(int)))
print(len(trainPredict.astype(int)))

# # 计算误差值/RMSE
# trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
# print('Train Score: %.2f RMSE' % (trainScore))
# testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
# print('Test Score: %.2f RMSE' % (testScore))

# print(testX)
# print(testY)
# plt.plot(trainY)
# plt.plot(trainPredict[1:])
# plt.show()
# plt.plot(testY)
# plt.plot(testPredict[1:])
# plt.show()

