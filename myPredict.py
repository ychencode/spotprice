from pandas import   Series
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model   import ARIMA
from math import sqrt
'''
series = Series.from_csv('robberies.csv', header=0)
split_point = len(series) - 12
dataset, validation = series[0:split_point], series[split_point:]
print('DataSet %d, Validation %d' % (len(dataset), len(validation)))
dataset.to_csv('dataset.csv')
validation.to_csv('validation.csv')
'''

'''
pyplot.figure(1)
pyplot.subplot(211)
series.hist()
pyplot.subplot(212)
series.plot(kind='kde')
pyplot.show()

series = Series.from_csv('dataset.csv')
X = series.values
X = X.astype('float32')
train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]

history = [x for x in train]
predictions = list()
for i in range (len(test)):
    yhat = history[-1]
    predictions.append(yhat)
    obs = test[i]
    history.append(obs)
    print('>Predicted=%.3f,   Expected=%3.f' % (yhat, obs))
mse = mean_squared_error(test, predictions)
rmse = sqrt(mse)
print('RMSE: %.3f' % rmse)

pyplot.figure(1)
pyplot.subplot(211)
series = Series.from_array(predictions)
series.plot()
pyplot.subplot(212)
series = Series.from_array(history)
series.plot()
pyplot.show()
'''

series = Series.from_csv('price.csv')
X = series.values
X = X.astype('float32')
train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]
history = [x for x in train]
predictions = list()
for i in range(len(test)):
    model = ARIMA(history, order=(0,1,2))
    model_fit = model.fit(disp=0)
    yhat = model_fit.forecast()[0]
    predictions.append(yhat)
    obs = test[i]
    history.append(obs)
    print('>Predicted=%.3f,   Expected=%3.f' % (yhat, obs))
mse = mean_squared_error(test, predictions)
rmse = sqrt(mse)
print('RMSE:   %.3f' % rmse)