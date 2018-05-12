import numpy as np
import pandas as pd
import xgboost

dataset = pd.read_csv('train.csv')

dataset['Family_size'] = dataset['SibSp']+dataset['Parch']

X = dataset.iloc[:,[2,4,5,12]].values
Y = dataset.iloc[:,1].values

from sklearn.preprocessing import Imputer
imp = Imputer()
X[:,[2]] = imp.fit_transform(X[:,[2]])

from sklearn.preprocessing import LabelEncoder
label_X = LabelEncoder()
X[:,1] = label_X.fit_transform(X[:,1])

from sklearn.preprocessing import OneHotEncoder
onehot_ = OneHotEncoder(categorical_features=[1])
X = onehot_.fit_transform(X).toarray()

X = X[:,[1,2,3,4]]

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X,Y)


# preparing the test set

dataset2 = pd.read_csv('test.csv')
dataset2['Family_size'] = dataset2['SibSp']+dataset2['Parch']

X_test = dataset2.iloc[:,[1,3,4,11]].values

imp2 = Imputer()
X_test[:,[2]] = imp2.fit_transform(X_test[:,[2]])

label_X2 = LabelEncoder()
X_test[:,1] = label_X2.fit_transform(X_test[:,1])

onehot_2 = OneHotEncoder(categorical_features=[1])
X_test = onehot_2.fit_transform(X_test).toarray()

X_test = X_test[:,[1,2,3,4]]

y_pred = classifier.predict(X_test)

y_val = dataset2.iloc[:,0].values

y_final = np.vstack([y_val,y_pred]).T

y_final = pd.DataFrame(y_final,columns=['PassengerId','Survived'])
y_final.to_csv('Test2.csv',index=False)