import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import joblib
data=pd.read_csv("website/diabetes.csv")
model=SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
X=data.iloc[:,:8]
y=data[["Outcome"]]
X=np.array(X)
y=np.array(y)

model = make_pipeline(StandardScaler(), RandomForestClassifier(random_state = 18))
model.fit(X,y.reshape(-1,))
joblib.dump(model,"model")