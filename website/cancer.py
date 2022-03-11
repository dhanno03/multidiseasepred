import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from xgboost import XGBClassifier
import joblib

data=pd.read_csv("website/cancer.csv")
data.drop(["Unnamed: 32"],axis="columns",inplace=True)

data.drop(["id"],axis="columns",inplace=True)
a=pd.get_dummies(data["diagnosis"])
cancer=pd.concat([data,a],axis="columns")
cancer.drop(["diagnosis","B"],axis="columns",inplace=True)
cancer.rename(columns={"M":"Malignant/Benign"},inplace=True)

y=cancer[["Malignant/Benign"]]
X=cancer.drop(["Malignant/Benign"],axis="columns")

X=np.array(X)
y=np.array(y)

model1=make_pipeline(StandardScaler(), XGBClassifier(random_state = 18))
model1.fit(X,y.reshape(-1,))

joblib.dump(model1,"model1")
