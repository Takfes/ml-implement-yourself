import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from trees import DTClassifier

dataset = load_breast_cancer()
X = dataset.get("data")
y = dataset.get("target")

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=2022)

dtc = DTClassifier()
dtc.fit(X_train,y_train)

skc = DecisionTreeClassifier()
skc.fit(X_train,y_train)

y_pred_dtc = dtc.predict(X_test)
y_pred_skc = skc.predict(X_test)

accuracy_score(y_test,y_pred_dtc)
accuracy_score(y_test,y_pred_skc)