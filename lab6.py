import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split
from keras import backend as K

def main():
    data = pd.read_csv("./dict1.csv", header = None, names = ["Angles", "XY"])
    print(data.head(10))

    train = data['Angles'].to_numpy()
    labels = data['XY'].to_numpy()

    X = list()
    Y = list()
    for i in range(len(train)):
        labels[i] = labels[i].replace('     ', ' ')
        labels[i] = labels[i].replace('   ', ' ')
        labels[i] = labels[i].replace('  ', ' ')
        labels[i] = labels[i].strip('[ ').strip(' ]')
        train[i] = train[i].strip('(').strip(')')
        result = [float(val) for val in train[i].split(',')]
        X.append(result)
        result = [float(val) for val in labels[i].split(' ')]
        Y.append(result)

    X_train, X_test, y_train, y_test = train_test_split(np.asarray(X), np.asarray(Y), test_size=0.80)

    print("TRAIN X SHAPE ", np.shape(X_train))
    print("TRAIN Y SHAPE ", np.shape(y_train))
    print("TEST X SHAPE ", np.shape(X_test))
    print("TEST Y SHAPE ", np.shape(y_test))
    
    def rmse(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred-y_true)))


    model = Sequential()
    model.add(Dense(10, input_dim =5, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(16, activation = 'tanh'))
    model.add(Dense(3, activation='linear'))
    model.compile(loss='mean_squared_logarithmic_error', optimizer=keras.optimizers.Adam(0.01))

    model.fit(X_train, y_train, epochs = 15)

    scores = model.evaluate(X_test, y_test, verbose=0)
    print("mean_squared_logarithmic_error: %.6f" % (scores))


    print(model.predict(X_train[10].reshape(1,3)))
    print(y_train[10])
    return


if __name__ == '__main__':
    main()
