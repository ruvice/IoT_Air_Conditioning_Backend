import numpy as np
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd
import pickle
import sqlite3
import csv

# Getting data from our rssi database
con = sqlite3.connect('rssidatabase.db')
outfile = open('rssivalues.csv', 'w', newline='')
outcsv = csv.writer(outfile)
cursor = con.execute('select * from rssi_model')

# dump column titles (optional)
outcsv.writerow(x[0] for x in cursor.description)
# dump rows
outcsv.writerows(cursor.fetchall())
outfile.close()


df = pd.read_csv('rssivalues.csv')

# Deal with missing data so algo recognises it as outlier
df.replace ('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['location'], 1))
y = np.array(df['location'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.2)

# clf = neighbors.KNeighborsClassifier(n_neighbors=1)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

# Test prediction
example_measures = np.array([[-999,-999,-999]])
example_measures = example_measures.reshape(len(example_measures), -1)

prediction = clf.predict(example_measures)
print(prediction)


# Saving model
# Its important to use binary mode 
knnPickle = open('knnpickle_file', 'wb') 

# source, destination 
pickle.dump(clf, knnPickle)                      
