import pandas as pd
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
 'edad':[18,22,35,45,52,23,40,60],
 'ingresos':[1000,1500,3000,4000,5000,1800,3500,6000],
 'clase':[0,0,1,1,1,0,1,1]
})

X = data[['edad','ingresos']]
y = data['clase']

model = Pipeline([
 ('scaler', StandardScaler()),
 ('svm', SVC(kernel='rbf', probability=True))
])
model.fit(X,y)
