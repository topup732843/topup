#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


data = pd.read_csv("C:\\Users\\krish\\Downloads\\sport.csv")
print(data,"n")


# In[6]:


d = np.array(data)[:,:-1]
print("n The attributes are: ",d)


# In[7]:


target = np.array(data)[:,-1]
print("n The target is: ",target)


# In[17]:


def train(c,t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
    return specific_hypothesis


# In[18]:


print("n The final hypothesis is:",train(d,target))


# In[ ]:




