import json

import re
mention_re=re.compile(r'@\S+')
hashtag_re=re.compile(r'#\S+')
url_re=re.compile(r'http\S+')
space_re=re.compile(r'\s+')

def clean_tweets(text):
    return space_re.sub(' ',url_re.sub(' ',hashtag_re.sub(' ',mention_re.sub(' ',text))).replace(' RT ',' ').lower()).strip()

def load_twitter_dataset(categories=['bs','hr','sr','me']):
    twitter_dataset=json.load(open('../data/Twitter-HBS.json'))
    X={'train':[],'dev':[],'test':[]}
    y={'train':[],'dev':[],'test':[]}
    for instance in twitter_dataset:
        lang=instance['language']
        split=instance['split']
        if lang in categories:
            y[split].append(lang)
            X[split].append(clean_tweets(' '.join(instance['tweets'])))
    return X,y

def load_setimes_dataset():
    setimes_dataset=json.load(open('../data/SETimes.HBS.json'))
    X={'train':[],'dev':[],'test':[]}
    y={'train':[],'dev':[],'test':[]}
    for instance in setimes_dataset:
        lang=instance['language']
        split=instance['split']
        y[split].append(lang)
        X[split].append(instance['text'].lower())
    return X,y
        