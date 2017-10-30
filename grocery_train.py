import struct
import numpy as np
from PIL import Image
import keras

from keras import backend as K
import pickle

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

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

#parameter

#Number_Classes = 27
batch_size = 1024
epochs = 1
depth = 1
max_features = 2127114
embedding_dims = 5


#Shape Data


#One hot encoding



#initialize model

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, 1024))
model.add(LSTM(dropout=0.2, recurrent_dropout=0.2))
model.add(LSTM(dropout=0.5, recurrent_dropout=0.5))
model.add(Dense(1, activation='relu'))

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

    
