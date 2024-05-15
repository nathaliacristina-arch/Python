#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# In[5]:


# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']) #Agg = Agregação.Nesse caso, ele retorna a média, desvio padrão e a contagem de registro


# In[ ]:




