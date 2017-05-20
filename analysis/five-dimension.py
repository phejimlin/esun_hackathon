import numpy as np
import better_exceptions
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


import json

from sklearn.preprocessing import normalize
import numpy as np

emo = [0, 1, 2, 3, 4, 5]
peo = [6]
sn = [7, 8, 9, 10]
risk = [11, 15]
idt = [12, 13, 14] + [ x for x in range(16, 43)]
feature_id = [emo, peo, sn, risk, idt]

#['emo_freq_sad', 'emo_freq_haha', 'emo_freq_wow', 'emo_freq_angry', 'emo_freq_love', 'emo_std', 'peo_review_num', 'sn_review_median', 'sn_review_mean', 'sn_review_std', 'sn_review_pos', 'risk_default', 'id_annual_income', 'id_employment_year', 'id_age', 'risk_score', 'id_occupation1', 'id_occupation10', 'id_occupation11', 'id_occupation12', 'id_occupation13', 'id_occupation14', 'id_occupation2', 'id_occupation3', 'id_occupation4', 'id_occupation5', 'id_occupation6', 'id_occupation7', 'id_occupation8', 'id_occupation9', 'id_education_level1', 'id_education_level2', 'id_education_level3', 'id_education_level4', 'id_education_level5', 'id_education_level6', 'id_education_level7', 'id_education_level8', 'id_resident_status0', 'id_resident_status1', 'id_resident_status2', 'id_resident_status3', 'id_resident_status4']

coef = logreg.coef_

five_mat = []
for user_mat in list(X_train):
	five = []
	for dim in feature_id:
		score = 0
		for idx in dim:
			if coef[idx] >0:
				score += coef[idx] * user_mat[idx]
			else:
				score += 1 - coef[idx] * user_mat[idx]
		five.append(score)
	credit = logreg.predict(user_mat)[0]
	five.append(credit)
	five_mat.append(five)

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0.1, 0.95),)
five_mat = min_max_scaler.fit_transform(np.array(five_mat))


user_data = json.load(open('user_profile_final.json', 'r'))
i=0
new_user_data = {}
for user_id, user in user_data.items():
	if 'review_num' not in user.keys():
		continue
	credit = user['total_score'] - user['good_score']
	if credit <= 0 : continue
	new_user_data[user_id] = user
print(len(new_user_data.keys()))
for user_id, user in new_user_data.items():
	user_mat = five_mat[i]
	credit = {
		'credit_matrix': list(user_mat[:5]),
		'credit_score': float(user_mat[5])
	}
	i+=1

	new_user_data[user_id].update(credit)

json.dump(new_user_data, open('user_profile_final_mat.json', 'w'))








