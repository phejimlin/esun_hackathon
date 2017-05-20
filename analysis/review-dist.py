import json

from sklearn.preprocessing import normalize
import numpy as np


user_data = json.load('user_profile_ruten_emo.json')
for user_id, user in user_data.items():
	if len(user) == 0: continue

	review = {}
	score = np.array(user['review_ruten']).astype('float32')
	l2_score = normalize(score)
	review['review_mean'] = np.mean(score)
	review['review_std'] = np.std(score)
	review['review_median'] = np.median(score)
	review['review_num'] = len(user['review_ruten'])

	threshold = 50/100
	vfunc = np.vectorize(lambda x: 1.0 if x >= threshold else 0.0)

	review['review_pos'] = np.sum(vfunc(score)) / review['review_num']

	del user_data[user_id]['review_ruten']
	user_data[user_id] += review


with open('user_profile_final.json', 'w') as f:
    json.dump(user_data, f)