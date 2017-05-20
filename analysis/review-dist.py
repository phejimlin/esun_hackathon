import json

from sklearn.preprocessing import normalize
import numpy as np


user_data = json.load(open('user_profile_ruten_emo.json', 'r'))
for user_id, user in user_data.items():
	if 'review_ruten' not in user.keys(): continue
	#print(user)
	review = {}
	score = np.array(user['review_ruten']).astype('float32').reshape(1, -1)
	l2_score = normalize(score)
	review['review_mean'] = float(np.mean(score))
	review['review_std'] = float(np.std(score))
	review['review_median'] = float(np.median(score))
	review['review_num'] = len(user['review_ruten'])

	threshold = 50/100
	vfunc = np.vectorize(lambda x: 1.0 if x >= threshold else 0.0)

	review['review_pos'] = int(np.sum(vfunc(score))) / review['review_num']
	#print(review)
	#print(score, l2_score)
	#break
	del user_data[user_id]['review_ruten']
	user_data[user_id].update(review)


with open('user_profile_final.json', 'w') as f:
    json.dump(user_data, f)
