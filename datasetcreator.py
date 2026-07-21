import pandas as pd
import numpy as np
import random
data=[]
for i in range(500):
    interests=random.randint(0,10)
    personality=random.randint(0,100)
    chats=random.randint(0,20)
    score=(5*interests+0.4*personality+chats*2+random.randint(-10,10))
    score=max(0,min(100,int(score)))
    data.append([interests,personality,chats,score])
df=pd.DataFrame(data,
                columns=["common_interests","personality_match","daily_chats","compatibility_score"])
df.to_csv("Dataset.csv",index=False)
print(df.head())
print("Dataset created successfully")
