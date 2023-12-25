from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd

# Load data
msg = pd.read_csv('NBC.csv', names=['message', 'label'])
msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})

# Split data
Xtrain, Xtest, ytrain, ytest = train_test_split(msg['message'], msg['labelnum'])

# Vectorize text data
count_v = CountVectorizer()
Xtrain_dm, Xtest_dm = count_v.fit_transform(Xtrain), count_v.transform(Xtest)

# Display a sample of the transformed data
print(pd.DataFrame(Xtrain_dm.toarray(), columns=count_v.get_feature_names_out())[:5])

# Train and predict using Naive Bayes
clf = MultinomialNB()
clf.fit(Xtrain_dm, ytrain)
pred = clf.predict(Xtest_dm)

# Display results
for doc, p in zip(Xtrain, pred):
    p = 'pos' if p == 1 else 'neg'
    print("%s -> %s" % (doc, p))

# Display accuracy metrics
print('\nAccuracy Metrics:')
print('Accuracy:', accuracy_score(ytest, pred))
print('Recall:', recall_score(ytest, pred))
print('Precision:', precision_score(ytest, pred))
print('Confusion Matrix:\n', confusion_matrix(ytest, pred))
