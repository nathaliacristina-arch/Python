#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ## Filtrando DataFrame do Pandas com Base em Strings
# 
# O Pandas oferece diversas funções para manipulação de strings. Começaremos com o filtros de strings com base nas letras iniciais e finais.

# In[5]:


# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
dsa_df[dsa_df.Segmento.str.startswith('Con')].head() #buscar todas as strings que começa com CON


# In[6]:


dsa_df.Segmento.value_counts()


# In[8]:


# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'MER'
dsa_df[dsa_df.Segmento.str.endswith('mer')].head()


# In[ ]:




