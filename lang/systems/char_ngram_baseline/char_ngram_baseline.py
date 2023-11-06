from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import json
from utils import load_twitter_dataset, load_setimes_dataset
from collections import Counter
from random import seed
seed(42)

clf=LinearSVC()

twitter_X,twitter_y=load_twitter_dataset()
twitter3_X,twitter3_y=load_twitter_dataset(['bs','hr','sr'])
setimes_X,setimes_y=load_setimes_dataset()

clf = Pipeline([
    ('vect', CountVectorizer(analyzer="char",ngram_range=(3,3))),
    ('clf', clf)
])

pred_report={'system':'char_ngram_baseline','predictions':[]}
preds=pred_report['predictions']

clf.fit(setimes_X['train'],setimes_y['train'])
print('setimes clf on setimes_test')
pred=clf.predict(setimes_X['test'])
preds.append({'train':'setimes','test':'setimes','predictions':pred.tolist()})
print(classification_report(setimes_y['test'],pred,digits=3))

print('setimes clf on twitter3_test')
pred=clf.predict(twitter3_X['test'])
preds.append({'train':'setimes','test':'twitter3','predictions':pred.tolist()})
print(classification_report(twitter3_y['test'],pred,digits=3))

clf.fit(twitter3_X['train'],twitter3_y['train'])
print('twitter3 clf on setimes_test')
pred=clf.predict(setimes_X['test'])
preds.append({'train':'twitter3','test':'setimes','predictions':pred.tolist()})
print(classification_report(setimes_y['test'],pred,digits=3))
print('twitter3 clf on twitter_test')
pred=clf.predict(twitter3_X['test'])
preds.append({'train':'twitter3','test':'twitter3','predictions':pred.tolist()})
print(classification_report(twitter3_y['test'],pred,digits=3))

clf.fit(twitter_X['train'],twitter_y['train'])
print('twitter clf on twitter_test')
pred=clf.predict(twitter_X['test'])
preds.append({'train':'twitter','test':'twitter','predictions':pred.tolist()})
print(classification_report(twitter_y['test'],pred,digits=3))
print(confusion_matrix(y_true=twitter_y["test"], y_pred=pred, labels="hr bs sr me".split()))

json.dump(pred_report,open('char_ngram_baseline.predictions.json','wt'))
