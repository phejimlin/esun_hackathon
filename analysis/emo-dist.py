import json

from sklearn.preprocessing import normalize
import numpy as np


emo_list = ['wow', 'haha', 'angry', 'love', 'sad']
user_emo = {}
user_data = json.load(open('user_profile_ruten.json', 'r'))
for emo_file in ['emo_fb_comments5.json', 'emo_fb_comments2.json']:
	emo_data = json.load(open(emo_file, 'r'))
	for user_url, item in emo_data.items():
		if len(item) == 0: continue
		emo_freq = {}
		for emo in emo_list:
			emo_freq[emo] = 0

		last_emo = []
		emo_consist = []
		for comment in item:

			emo_freq[comment['emotion1']] += 1
			emo_freq[comment['emotion2']] += 1
			emo_consist += [1 if comment['emotion1'] in last_emo or comment['emotion2'] in last_emo else 0]
			last_emo = [comment['emotion1'], comment['emotion2']]

		norm_emo_freq = normalize(np.array(list(emo_freq.values())).reshape(1, -1), axis=1)
		emo_std = np.array(emo_consist).std()
		
		try:
			user = user_url.split('?s=')[-1]
			user_data[user]
		except:
			print('err')
			continue

		user_data[user]['norm_emo_freq'] = list(norm_emo_freq[0])
		user_data[user]['emo_std'] = float(emo_std)

with open('user_profile_ruten_emo.json', 'w') as f:
    json.dump(user_data, f)
