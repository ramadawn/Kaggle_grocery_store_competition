import struct
import numpy as np
from PIL import Image

import pickle

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD

#import in dataset

def unpickle(filename):

    pickle_in_Data = open("Cleaned_Training_Labels1.pickle", "rb")
    data_list = pickle.load(pickle_in_Data)

    return data_list

Train_data = unpickle("Cleaned_Training_Data1.pickle")
Test_data = unpickle("Cleaned_Testing_Data1.pickle")
Train_labels = unpickle("Cleaned_Training_Labels1.pickle")
Test_labels = unpickle("Cleaned_Testing_Labels1.pickle")

Train_data = np.asarray(Train_data, dtype=object) 
Test_data = np.asarray(Test_data, dtype=object)
Train_labels = np.asarray(Train_labels, dtype=object)
Test_labels = np.asarray(Test_labels, dtype=object)

#Train_data = np.reshape(Train_data.shape,1)
#Test_data = np.reshape(Test_data.shape,1)
#Train_labels = np.reshape(Test_labels.shape,1)
#Test_labels = np.reshape(Test_labels.shape,1)

print(Train_data.shape)

#parameter

#Number_Classes = 27
batch_size = 1024
epochs = 1
depth = 1
num_classes = 2127114
data_dim = 16
timesteps = 8



#Shape Data


#One hot encoding



#initialize model

print('Build model...')

model = Sequential()
model.add(Dense(num_classes, activation='relu', input_shape= 289416, 1))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(Train_data, Train_labels,
          batch_size=batch_size,
          epochs=epochs,  verbose=1,
          validation_data=(Train_data, Train_labels))

score, acc = model.evaluate(Train_data, Train_labels,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)

#save the model
#serialize model to jason
model_json = model.to_json()
with open("EMmodel.json", "w") as json_file:
          json_file.write(model_json)

#serialize weights to HDF5
model.save_weights("EMmodel.h5")



print('ok')














##for line in range(10):
##    current_img = file[line]
##    print(current_img)
##    img = Image.fromarray(current_img)
##    img.show()
##    print("label = ", label[line])
##    input()
   


##img = Image.fromarray(data, 'RGB')
##img.save('my.png')
##img.show()

    
