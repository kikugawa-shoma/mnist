import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_valid,x_test,y_valid,y_test = train_test_split(x_test,y_test,test_size=0.2)
x_train = x_train.reshape(x_train.shape[0],28*28)
x_train = x_train.astype("float32")
x_train = x_train/255
x_test = x_test.reshape(x_test.shape[0],28*28)
x_test = x_test.astype("float32")
x_test /= 255
y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)



model = Sequential()
model.add(Dense(10,input_shape=(28*28,)))

opt = keras.optimizers.Adam()
loss_fn = "categorical_crossentropy"

model.compile(optimizer=opt,loss=loss_fn)
model.fit(x_train,y_train,epochs=5,batch_size=32)
loss_and_metrics = model.evaluate(x_test,y_test,batch_size=128)