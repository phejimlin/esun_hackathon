import numpy as np
np.random.seed(1337)

X_train = np.load('creditM-X-data.npy').astype('float32')
Y_train = np.load('creditM-Y-data.npy').astype('float32')

''' Shuffle training data '''
'''
from sklearn.utils import shuffle
X_train,Y_train = shuffle(X_train,Y_train,random_state=1337)
'''

from sklearn import linear_model
logreg = linear_model.LinearRegression(n_jobs=-1)

logreg.fit(X_train, Y_train)


from sklearn.metrics import mean_squared_error
pred_y = logreg.predict(X_train)
print(np.sort(pred_y, axis=0))

print('mse',mean_squared_error(Y_train, pred_y))

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
blah_y = min_max_scaler.fit_transform(pred_y).reshape(-1)
print(blah_y)
np.savetxt("pred_credit_lr.csv", blah_y, delimiter=",")
np.save('cm-lr-coef', logreg.coef_)
#print('confusion matrix')
#print(confusion_matrix(Y_train, pred_y))

'''
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
'''

''' Visualize the loss and accuracy of both models'''
risk_score = np.genfromtxt('risk_score.csv', delimiter=',')
print(risk_score[:, 2].shape)

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
y_set = np.array([Y_train, pred_y, blah_y, risk_score[:, 2]])
#y_set = np.sort(y_set[0], axis=0)
#y_set = sorted(y_set, key=lambda x: x[0]) 
idx = np.argsort(y_set[0])
y_set=y_set[:,idx]

print(y_set)

plt.figure(1)
plt.plot(range(len(y_set[0])), y_set[0],label='y_true')
plt.plot(range(len(y_set[0])), y_set[1],label='y_pred')
plt.plot(range(len(y_set[0])), y_set[2],label='y_adj_credit')
plt.legend(loc='lower right')
plt.savefig('pred-credit-3.png',dpi=150,format='png')
plt.close()
print('Result saved into 05_overfittingCheck.png')
