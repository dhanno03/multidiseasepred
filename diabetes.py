import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.tree import DecisionTreeClassifier
data=pd.read_csv("diabetes.csv")
model=SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
X=data.iloc[:,:8]
y=data[["Outcome"]]
X=np.array(X)
y=np.array(y)

model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)
model.fit(X,y.reshape(-1,))
joblib.dump(model,"model")