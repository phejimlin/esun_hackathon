import numpy as np
np.random.seed(1337)

X_train = np.load('X_training.npy').astype('int')
Y_train = np.load('Y_training.npy').astype('float32')*0.1


''' Shuffle training data '''
from sklearn.utils import shuffle
X_train,Y_train = shuffle(X_train,Y_train,random_state=1337)

''' set the size of mini-batch and number of epochs'''
import sys
batch_size = int(sys.argv[1])
nb_epoch = int(sys.argv[2])

''' use tensorflow as backend '''
import tensorflow as tf
sess = tf.Session()

from keras import backend as K
K.set_session(sess)

''' Import keras to build a DL model '''
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras import regularizers

print('Building a model whose optimizer=adam, activation function=softplus')
model_adam = Sequential()
model_adam.add(Dense(128, input_dim=X_train[0].shape[0], 
	kernel_regularizer=regularizers.l2(0.01)))
model_adam.add(Activation('relu'))
model_adam.add(Dropout(0.5))
model_adam.add(Dense(256))
model_adam.add(Activation('softplus'))
model_adam.add(Dense(1))
model_adam.add(Activation('sigmoid'))

''' Setting optimizer as Adam '''
from keras.optimizers import SGD, Adam, RMSprop, Adagrad
model_adam.compile(loss= 'mean_squared_error',
              		optimizer='Adam',
              		metrics=['accuracy'])

with tf.device('/gpu:0'):
	'''Fit models and use validation_split=0.1 '''
	history_adam = model_adam.fit(X_train, Y_train,
								batch_size=batch_size,
								epochs=nb_epoch,
								verbose=1,
								shuffle=True,
								validation_split=0.3)

model_adam.save_weights('weights.hdf5')

from sklearn.metrics import confusion_matrix, accuracy_score
pred_y = model_adam.predict(X_train)
print(pred_y[:10])
#print('confusion matrix')
#print(confusion_matrix(Y_train, pred_y))

print('confusion matrix')
print(confusion_matrix(np.rint(Y_train), np.rint(pred_y)))
print('accuracy', accuracy_score(np.rint(Y_train), np.rint(pred_y)))

#threshold = 0.7
for i in range(50, 100, 5):
	threshold = i/100
	vfunc = np.vectorize(lambda x: 1.0 if x >= threshold else 0.0)
	print('threshold = {0} confusion matrix'.format(threshold))
	print(confusion_matrix(vfunc(Y_train), vfunc(pred_y)))
	print('accuracy', accuracy_score(vfunc(Y_train), vfunc(pred_y)))

loss_adam= history_adam.history.get('loss')
acc_adam = history_adam.history.get('acc')

''' Access the performance on validation data '''
val_loss_adam = history_adam.history.get('val_loss')
val_acc_adam = history_adam.history.get('val_acc')

''' Visualize the loss and accuracy of both models'''
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.figure(0)
plt.subplot(121)
plt.plot(range(len(loss_adam)), loss_adam,label='Training')
plt.plot(range(len(val_loss_adam)), val_loss_adam,label='Validation')
plt.title('Loss')
plt.legend(loc='upper left')
plt.subplot(122)
plt.plot(range(len(acc_adam)), acc_adam,label='Training')
plt.plot(range(len(val_acc_adam)), val_acc_adam,label='Validation')
plt.title('Accuracy')
plt.savefig('05_overfittingCheck.png',dpi=300,format='png')
plt.close()
print('Result saved into 05_overfittingCheck.png')
