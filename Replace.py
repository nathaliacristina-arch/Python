#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ## Replace de Strings em DataFrames do Pandas
# 
# Se for necessário substituir caracteres dentro de uma string o Pandas oferece uma função para isso também.
# 
# Por exemplo, vamos substituir 2 caracteres em uma das colunas.

# In[4]:


# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX') #Replace = Substituição


# In[5]:


dsa_df.head()


# In[ ]:




