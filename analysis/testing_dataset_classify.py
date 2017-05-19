
# coding: utf-8

# In[1]:


import os,sys
import json
import operator
import jieba
import numpy as np

from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer


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


# In[27]:




# In[28]:



# In[29]:




# In[30]:




# In[31]:



# In[ ]:

if __name__ == "__main__":
    folder_path = 'ruten_comments/'
    dirs = os.listdir(folder_path)


    corpus = []
    comment_scores = []
    for doc in dirs:
        data = load_data(doc)
        for seller, info in data.items():
            if len(info) != 0:
                for items in info:
                    for item in items:
                        score_type = item['point']
                        if score_type == 'good' or score_type == 'bad':
                            comment = item['content'][0]
                            if 'content' in comment:
                                soup = BeautifulSoup(comment['content'], "lxml")
                                comment_text = soup.getText()
                                length = len(comment_text)
                                if length > 13:
                                    corpus.append(' '.join(jieba.cut(comment_text, cut_all=False)))

                                    if score_type == 'good':
                                        comment_scores.append(1.0)
                                    if score_type == 'bad':
                                        comment_scores.append(0.0)
        break



    tfidf_vectorizer = TfidfVectorizer()
    tfidf = tfidf_vectorizer.fit_transform(corpus)
    tfidf_features = tfidf_vectorizer.get_feature_names()

    sorted_scores = display_scores(tfidf_vectorizer, tfidf)

    bag_of_words = [word[0] for word in sorted_scores[:198]]
    top_n = np.array(bag_of_words)
    np.save('top_n.npy', top_n)


    testing_set = []
    for sentence in corpus:
        features = []
        for word in bag_of_words:
            if word in sentence.split(' '):
                features.append(1)
            else:
                features.append(0)
        testing_set.append(features)


    X = np.array(testing_set)
    Y = np.array(comment_scores)
    np.save('ruten_X_testing.npy', X)
    np.save('ruten_Y_testing.npy', Y)









