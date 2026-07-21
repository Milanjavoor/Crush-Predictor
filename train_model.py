import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib


df=pd.read_csv(r"C:\Users\ADMIN\3D Objects\LAB\Dataset.csv")

x=df.drop(columns=["compatibility_score"],axis=1)
y=df["compatibility_score"]

x_train,x_test,y_train,y_test=train_test_split(x,y,
                                               random_state=42,
                                               test_size=0.3)
model=RandomForestRegressor(n_estimators=100,random_state=42)

model.fit(x_train,y_train)
score=model.score(x_test,y_test)

print("Model accuracy:",score)

joblib.dump(model,"compactibility_model.pkl")
print("Model successfully loaded")