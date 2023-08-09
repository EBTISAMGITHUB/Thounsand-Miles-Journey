#!/usr/bin/env python
# coding: utf-8

# # Python 2nd Task
# 
# ## ادراج البيانات في Jupyter وطباعتها
# 
# ### Link data --> https://www.kaggle.com/datasets/joebeachcapital/gpa-and-iq?resource=download

# In[10]:


import numpy as np
import pandas as pd


df = pd.read_csv('gpa_iq.csv')
df.head()

df[["gpa", "iq", "concept"]].describe()

