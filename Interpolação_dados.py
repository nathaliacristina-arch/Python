#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Importando o NumPy
import numpy as np


# In[6]:


import pandas as pd


# In[7]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[8]:


dsa_df.head(5)


# In[11]:


#Faz a soma de todos os valores ausentes existentes 
dsa_df.isna().sum()


# In[12]:


# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]


# In[14]:


#A moda em Estatística é uma medida de tendência central que representa o valor mais frequente em um conjunto de dados. 

moda


# In[17]:


# E por fim preenchemos os valores NA com a moda, fillna= Preenche os valores que estão ausentes com o valor da moda
#inplace = true faz a modificação no data frame que estamos usando e não em uma cópia
dsa_df['Quantidade'].fillna(value = moda, inplace = True)


# In[18]:


dsa_df.isna().sum()


# In[ ]:




