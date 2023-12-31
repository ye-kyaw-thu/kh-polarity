## Decision Tree Classifier for Khmer Polarity
## Written by Ye Kyaw Thu, 
## Affiliate Professor, IDRI, CADT, Cambodia
## Used for 4th NLP/AI Workshop, Chiang Mai, Experiment
## Last updated: 8 Feb 2023
## Reference:
## https://towardsdatascience.com/building-a-sentiment-classifier-using-scikit-learn-54c8e7c5d2f0
## https://vitalflux.com/accuracy-precision-recall-f1-score-python-example/  
## https://stackoverflow.com/questions/62792001/precision-and-recall-are-the-same-within-a-model
## https://towardsdatascience.com/micro-macro-weighted-averages-of-f1-score-clearly-explained-b603420b292f
## https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html

import pandas as pd
import re
from os import system, listdir
from os.path import isfile, join
from random import shuffle

import warnings
warnings.filterwarnings("ignore")


polar_train = pd.read_csv('csv/train.csv')
polar_test = pd.read_csv('csv/test.csv')

### Text Vectorization

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from joblib import dump, load # used for saving and loading sklearn objects
from scipy.sparse import save_npz, load_npz # used for saving and loading sparse matrices

system("mkdir 'data_preprocessors'")
system("mkdir 'vectorized_data'")


# Unigram Counts

unigram_vectorizer = CountVectorizer(ngram_range=(1, 1))
unigram_vectorizer.fit(polar_train['text'].values)

dump(unigram_vectorizer, 'data_preprocessors/unigram_vectorizer.joblib')

# unigram_vectorizer = load('data_preprocessors/unigram_vectorizer.joblib')

X_train_unigram = unigram_vectorizer.transform(polar_train['text'].values)

save_npz('vectorized_data/X_train_unigram.npz', X_train_unigram)

# X_train_unigram = load_npz('vectorized_data/X_train_unigram.npz')


# Unigram Tf-Idf

unigram_tf_idf_transformer = TfidfTransformer()
unigram_tf_idf_transformer.fit(X_train_unigram)

dump(unigram_tf_idf_transformer, 'data_preprocessors/unigram_tf_idf_transformer.joblib')

# unigram_tf_idf_transformer = load('data_preprocessors/unigram_tf_idf_transformer.joblib')

X_train_unigram_tf_idf = unigram_tf_idf_transformer.transform(X_train_unigram)

save_npz('vectorized_data/X_train_unigram_tf_idf.npz', X_train_unigram_tf_idf)

# X_train_unigram_tf_idf = load_npz('vectorized_data/X_train_unigram_tf_idf.npz')


# Bigram Counts

bigram_vectorizer = CountVectorizer(ngram_range=(1, 2))
bigram_vectorizer.fit(polar_train['text'].values)

dump(bigram_vectorizer, 'data_preprocessors/bigram_vectorizer.joblib')

# bigram_vectorizer = load('data_preprocessors/bigram_vectorizer.joblib')

X_train_bigram = bigram_vectorizer.transform(polar_train['text'].values)

save_npz('vectorized_data/X_train_bigram.npz', X_train_bigram)

# X_train_bigram = load_npz('vectorized_data/X_train_bigram.npz')


# Bigram Tf-Idf

bigram_tf_idf_transformer = TfidfTransformer()
bigram_tf_idf_transformer.fit(X_train_bigram)

dump(bigram_tf_idf_transformer, 'data_preprocessors/bigram_tf_idf_transformer.joblib')

# bigram_tf_idf_transformer = load('data_preprocessors/bigram_tf_idf_transformer.joblib')

X_train_bigram_tf_idf = bigram_tf_idf_transformer.transform(X_train_bigram)

save_npz('vectorized_data/X_train_bigram_tf_idf.npz', X_train_bigram_tf_idf)

# X_train_bigram_tf_idf = load_npz('vectorized_data/X_train_bigram_tf_idf.npz')

### Choosing the Data Format


from sklearn.model_selection import train_test_split
from scipy.sparse import csr_matrix
import numpy as np

# Import logistic regression library
from sklearn import tree
from sklearn.metrics import classification_report

def train_and_show_scores_DTREE(X: csr_matrix, y: np.array, title: str, model: str) -> None:
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, train_size=0.75, stratify=y
    )

    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    valid_score = clf.score(X_valid, y_valid)
    print(f'{title}\nTrain score: {round(train_score, 2)} ; Validation score: {round(valid_score, 2)}\n')

    #saving model
    dump(clf, 'classifiers/' + model)

y_train = polar_train['label'].values

train_and_show_scores_DTREE(X_train_unigram, y_train, 'DTREE, Unigram Counts', 'dtree_unigram_count.joblib')
train_and_show_scores_DTREE(X_train_unigram_tf_idf, y_train, 'DTREE, Unigram Tf-Idf', 'dtree_unigram_tf-idf.joblib')
train_and_show_scores_DTREE(X_train_bigram, y_train, 'DTREE, Bigram Counts', 'dtree_bigram_count.joblib')
train_and_show_scores_DTREE(X_train_bigram_tf_idf, y_train, 'DTREE, Bigram Tf-Idf', 'dtree_bigram_tf-idf.joblib')


### Testing/Evaluation

X_test = unigram_vectorizer.transform(polar_test['text'].values)
X_test = unigram_tf_idf_transformer.transform(X_test)
y_test = polar_test['label'].values

dtree_unigram_counts = load('classifiers/dtree_unigram_count.joblib')
score = dtree_unigram_counts.score(X_test, y_test)
print('Decision Tree Test Result, Unigram Counts: ', score)

# Predict the class of test set
y_predict = dtree_unigram_counts.predict(X_test)

err_rate = (y_predict != y_test).mean()
print('Error Rate: %.2f' % err_rate)
print('----------')
print(classification_report(y_test, y_predict))
print('')

dtree_unigram_tfidf = load('classifiers/dtree_unigram_tf-idf.joblib')
score = dtree_unigram_tfidf.score(X_test, y_test)
print('Decision Tree Test Result, Unigram Tf-Idf: ', score)

# Predict the class of test set
y_predict = dtree_unigram_tfidf.predict(X_test)

err_rate = (y_predict != y_test).mean()
print('Error Rate: %.2f' % err_rate)
print('----------')
print(classification_report(y_test, y_predict))
print('')

X_test = bigram_vectorizer.transform(polar_test['text'].values)
X_test = bigram_tf_idf_transformer.transform(X_test)
y_test = polar_test['label'].values

dtree_bigram_counts = load('classifiers/dtree_bigram_count.joblib')
score = dtree_bigram_counts.score(X_test, y_test)
print('Decision Tree Test Result, Bigram Count: ', score)

# Predict the class of test set
y_predict = dtree_bigram_counts.predict(X_test)

err_rate = (y_predict != y_test).mean()
print('Error Rate: %.2f' % err_rate)
print('----------')
print(classification_report(y_test, y_predict))
print('')

dtree_bigram_tfidf = load('classifiers/dtree_bigram_tf-idf.joblib')
score = dtree_bigram_tfidf.score(X_test, y_test)
print('Decision Tree Test Result, Bigram Tf-Idf: ', score)

# Predict the class of test set
y_predict = dtree_bigram_tfidf.predict(X_test)

err_rate = (y_predict != y_test).mean()
print('Error Rate: %.2f' % err_rate)
print('----------')
print(classification_report(y_test, y_predict))
print('')
