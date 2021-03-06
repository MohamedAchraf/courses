# -*- coding: utf-8 -*-
"""CNN_04_MAXPOOLING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16RDr2WI3b-Zr8ifW1iLVkbP3yCokPSjI

# <div align = center>CIFAR 10:  مجموعة الصور الملونة المصنفة إلى 10 فئات.

<hr>

#1 - المكتبات (Librairies)
"""

from keras.datasets import cifar10 as DS
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy
import matplotlib.pyplot as plt

"""# 2 - البيانات  (Data)

## 2.1 - تحميل البيانات
"""

(x_train, y_train),(x_test, y_test) = DS.load_data()

print("x_train shape =" , x_train.shape)
print("y_train shape =" , y_train.shape)

print("\nx_test shape =" , x_test.shape)
print("y_test shape =" , y_test.shape)

"""## 2.2 - عرض عينة من البيانات"""

figure = plt.figure()

for i in range(25):
  figure.add_subplot(5, 5, i+1)
  plt.imshow(x_train[i])

plt.show()

"""## 2.3 -  تغيير شكل المخرجات"""

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

"""# 3- الشبكة العصبية

## 3.1.1 -  النموذج بدون تجميع
"""

model = Sequential([
              Conv2D( 32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(32,32,3)),
              Conv2D( 64, (3, 3), padding='valid', activation='relu'),
              Conv2D(128, (3, 3), padding='valid', activation='relu'),
              Conv2D(256, (3, 3), padding='valid', activation='relu'),

              Flatten(),        
                     
              Dense(1025, activation='relu'),              
              Dense(512, activation='relu'),              
              Dense(256, activation='relu'),              
              Dense(128, activation='relu'),               
              Dense(10, activation='softmax')

])

print(model.summary())

"""## 3.1.1 -  النموذج مع تجميع"""

model = Sequential([
              Conv2D( 32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(32,32,3)),
              MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'),

              Conv2D( 64, (3, 3), padding='valid', activation='relu'),
              MaxPooling2D(pool_size=(2,2), strides=1, padding='valid'),

              Conv2D(128, (3, 3), padding='valid', activation='relu'),
              MaxPooling2D(pool_size=(2,2), strides=1, padding='valid'),

              Conv2D(256, (3, 3), padding='valid', activation='relu'),
              MaxPooling2D(pool_size=(2,2), strides=1, padding='valid'),

              Flatten(),        
                     
              Dense(1025, activation='relu'),              
              Dense(512, activation='relu'),              
              Dense(256, activation='relu'),              
              Dense(128, activation='relu'),               
              Dense(10, activation='softmax')

])

print(model.summary())

"""## 3.2 -  تركيب النموذج """

model.compile(
    optimizer = Adam(learning_rate=0.001),
    loss = categorical_crossentropy,
    metrics=['accuracy']
)

"""## 3.3 - تدريب النموذج


"""

nb_epochs = 7

history = model.fit(x_train, y_train, batch_size=128, epochs=nb_epochs, verbose=1, validation_split=0.2)

"""## 3.4 -  التقييم

"""

loss, acc = model.evaluate(x_test, y_test, verbose=1)
print("Accuracy = %0.2f" % (acc*100), "%")

"""## 3.5 -  الرسوم البيانية للتعلم

"""

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.rcParams["figure.figsize"] = (17,7)
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 
plt.rcParams["figure.figsize"] = (17,7)
plt.show()