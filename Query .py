#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando o NumPy
import numpy as np


# In[2]:


import pandas as pd


# Com o Pandas criamos dataframes, que são essencialmente tabelas. Como tal, podemos fazer consultas, ou simplesmente queries. E para isso usamos o método query(). 

# In[3]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[4]:


dsa_df.head()


# In[5]:


# Checamos os valores mínimo e máximo da coluna Valor_Venda
dsa_df.Valor_Venda.describe()


# In[6]:


# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')


# In[7]:


# Então confirmamos os valores mínimo e máximo
df2.Valor_Venda.describe()


# In[8]:


# Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')


# In[9]:


df3.head()


# In[ ]:





# In[ ]:




