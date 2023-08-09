#!/usr/bin/env python
# coding: utf-8

# # Python Code Task for Adding  data & scatter_plot
# 
# ### Link data --> https://www.kaggle.com/datasets/joebeachcapital/gpa-and-iq?resource=download

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gpa_iq.csv')
df.head()

df[["gpa", "iq", "concept"]].describe()

plt.scatter(df[["gpa"]], df[["iq"]])
plt.show()

