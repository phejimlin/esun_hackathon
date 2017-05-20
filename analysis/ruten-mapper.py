
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
model_adam.add(Dense(128, input_dim=198, 
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

model_adam.load_weights('best_mdl.hdf5')

user_data = json.load(open('APIscore_from_ruten.json', 'r'))

if __name__ == "__main__":
    folder_path = 'ruten_comments/'
    dirs = os.listdir(folder_path)


    corpus = list(np.load('top_n.npy'))
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
                        if 'content' in comment:
                            soup = BeautifulSoup(comment['content'], "lxml")
                            comment_text = soup.getText()
                            length = len(comment_text)
                            if length > 13:
                                word_list = list(jieba.cut(comment_text, cut_all=False))
                                vec = []
                                for word in corpus:
                                    value = 1 if word in word_list else 0
                                    vec.append(value)
                                score = '%.2f' % float(model_adam.predict(np.array([vec]))[0])
                                try:
                                    user_data[seller]
                                except:
                                    continue

                                try:
                                    user_data[seller]['review_ruten'].append(score)
                                except:
                                    user_data[seller]['review_ruten'] = [score]
        #break
with open('user_profile_ruten.json', 'w') as f:
    json.dump(user_data, f)
    









