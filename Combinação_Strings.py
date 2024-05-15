#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ## Combinação de Strings em DataFrames do Pandas
# 
# A função cat() pode ser usada para concatenar strings em um dataframe do Pandas.
# 
# Vamos criar uma nova coluna concatenando as colunas “ID_Pedido” e “Segmento” com o separador “-”.

# In[4]:


dsa_df.head()


# In[7]:


# Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-') #cat = combinação , cria uma nova coluna pedido_segmento, ou seja, concatena as duas colunas e coloca ela em uma nova coluna


# In[8]:


dsa_df.head()


# In[ ]:




