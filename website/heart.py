import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

data = pd.read_csv("website/heart.csv")
data["trestbps"]=np.log(data["trestbps"])

data=data.drop(["fbs"],axis=1)
data=data.drop(["ca"],axis=1)
data["chol"]=np.log(data["chol"])
y=data["target"]

np.random.shuffle(data.values)
X=data.drop(["target"],axis=1)

X=np.array(X)
y=np.array(y)

model2= make_pipeline(StandardScaler(), RandomForestClassifier(random_state = 18))
model2.fit(X,y.reshape(-1,))
joblib.dump(model2,"model2")