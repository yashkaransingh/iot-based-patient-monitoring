#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('C:\\Users\\Pradyot\\Downloads\\IoT_Patient_Monitor_Data.csv')
df


# In[35]:


import matplotlib.pyplot as plt
values = np.array(df['oxygen'])
age = np.array(df['age'])
plt.scatter(age, values)
plt.show()


# In[36]:


HR = np.array(df['heartrate'])
age = np.array(df['age'])
plt.scatter(age, HR)
plt.show()


# In[67]:


conditions=[
    (df['oxygen']>=95) & (df['heartrate']>=100) & (df['age']>=20) & (df['age']<30), #normal
    (df['oxygen']<95)  & (df['heartrate']>100)  & (df['age']>=20) & (df['age']<30), #low oxygen
    (df['oxygen']>=95) & (df['heartrate']<100) & (df['age']>=20) & (df['age']<30), #low Heartrate
    (df['oxygen']<95) & (df['heartrate']<100) & (df['age']>=20) & (df['age']<30), #low oxy,low heartrate
    (df['oxygen']>=95) & (df['heartrate']>=93) & (df['age']>=30) & (df['age']<40), #normal
    (df['oxygen']<95) & (df['heartrate']>=93) & (df['age']>=30) & (df['age']<40), #low oxygen
    (df['oxygen']>=95) & (df['heartrate']<93) & (df['age']>=30) & (df['age']<40), #low heart rate
    (df['oxygen']<95) & (df['heartrate']<93) & (df['age']>=30) & (df['age']<40), #low oxy,low heartrate
    (df['oxygen']>=95) & (df['heartrate']>88) & (df['age']>=40) & (df['age']<50), #normal
    (df['oxygen']<95) & (df['heartrate']>88) & (df['age']>=40) & (df['age']<50), #low oxygen
    (df['oxygen']>=95) & (df['heartrate']<88) & (df['age']>=40) & (df['age']<50), #low heart rate
    (df['oxygen']<95) & (df['heartrate']<88) & (df['age']>=40) & (df['age']<50) #low oxy,low heartrate


]
values=['Normal','Low Oxygen','Low HeartRate','Low Oxygen and Low HeartRate','Normal','Low Oxygen','Low HeartRate','Low Oxygen and Low HeartRate','Normal','Low Oxygen','Low HeartRate','Low Oxygen and Low Heartrate']
df['Status'] = np.select(conditions,values)
df


# In[68]:


df.Status.value_counts().plot(kind="barh")


# In[80]:


from  sklearn.tree import DecisionTreeClassifier
df.info()


# In[91]:


from sklearn.metrics import accuracy_score
X = df.drop(['created_at','Status','entry_id'],axis=1)
Y= df['Status']
model = DecisionTreeClassifier()
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3)
model.fit(X_train,Y_train)
predictions = model.predict(X_test)
print("Predictions : \n")
print(predictions)
accuracy = accuracy_score(predictions,Y_test)
# actual_accuracy = accuracy*100
print("\n")
print("accuracy : \n")
print(accuracy)
print("\n")


# In[ ]:
