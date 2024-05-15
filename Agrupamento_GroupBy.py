#!/usr/bin/env python
# coding: utf-8

# ## Agrupamento de Dados em DataFrames com Group By
# 
# A função Pandas Groupby é uma função versátil e fácil de usar que ajuda a obter uma visão geral dos dados. Isso torna mais fácil explorar o conjunto de dados e revelar os relacionamentos entre as variáveis.
# 
# O código a seguir agrupará as linhas com base nas combinações Segmento/Regiao/Valor_Venda e nos dará a taxa média de vendas de cada grupo.

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# In[5]:


# Aplicamos o group by
dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()  #Somente as tres colunas, agrupamento pelas duas colunas que não possuem numero e calcula a média pela ultima


# In[ ]:




