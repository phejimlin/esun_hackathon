
# coding: utf-8

# In[1]:


import os,sys
import json
import operator
import jieba
import numpy as np

from bs4 import BeautifulSoup


# In[4]:

def load_data(file_name):
    with open('ruten_comments/{0}'.format(file_name)) as data_file:
        data = json.load(data_file)
        return data


# In[5]:




# In[23]:




# In[26]:

def display_scores(vectorizer, tfidf_result):
    # http://stackoverflow.com/questions/16078015/
    scores = zip(vectorizer.get_feature_names(),
                 np.asarray(tfidf_result.sum(axis=0)).ravel())
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    index_scores = []
    for index, item in enumerate(sorted_scores):
        index_scores.append((index, item[1]))
        
    #generate_bar_chart(index_scores, 'TFIDF Score')
    return sorted_scores


user_data = json.load(open('APIscore_from_ruten.json', 'r'))

if __name__ == "__main__":
    folder_path = 'ruten_comments/'
    dirs = os.listdir(folder_path)


    comment_scores = []
    for doc in dirs:
        print(doc)
        data = load_data(doc)
        X_data = []
        Y_data = []
        for seller, info in data.items():
            if len(info) != 0:
                
                for items in info:
                    for item in items:
                        try:
                            score_type = item['point']
                        except:
                            continue
                        comment = item['content'][0]
                        user = item['user']
                        date = item['date']
                        if 'content' in comment:
                            soup = BeautifulSoup(comment['content'], "lxml")
                            comment_text = soup.getText()
                            length = len(comment_text)
                            if length > 13:
                                try:
                                    user_data[seller]['review_contents'].append({'user':user, 'date': date, 'content': comment_text})
                                except:
                                    user_data[seller]['review_contents'] = [{'user':user, 'date': date, 'content': comment_text}]
        #break
with open('user_profile_comments.json', 'w') as f:
    json.dump(user_data, f)
    









