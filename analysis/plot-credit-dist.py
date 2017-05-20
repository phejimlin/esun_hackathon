import numpy as np


y = np.load('creditM-Y-data.npy')
d = np.sort(y)

''' Visualize the loss and accuracy of both models'''
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.figure(0)
plt.plot(range(len(d)), d,label='credit dist')
plt.savefig('diff-credit.png',dpi=72,format='png')
plt.close()
print('Result saved into 05_overfittingCheck.png')
print(d)