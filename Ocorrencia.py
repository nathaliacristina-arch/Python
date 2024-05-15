#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ### Verificando a Ocorrência de Diversos Valores em Uma Coluna
# 
# Em nosso conjunto de dados de exemplo temos a coluna Quantidade que representa a quantidade de itens vendidos em cada uma das vendas. Imagine que precisamos saber em quais vendas foram vendidos 5, 7, 9 ou 11 itens.
# 
# Como aplicaríamos esse tipo de filtro ao nosso dataframe?
# 
# Fácil. O Pandas oferece o método isin() para checar diversos valores em uma coluna. Quem conhece Linguagem SQL já deve ter percebido que o método é o mesmo que a cláusula IN em SQL. Vamos ao exemplo.

# In[4]:


dsa_df.shape #numero de linhas, numero de colunas


# In[6]:


# Então aplicamos o filtro, verifica se na coluna VENDAS há 5, 7, 9, 11 vendas, ou seja, quantidade igual a 5, 7, 9, 11
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])]


# In[7]:


# Shape
dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape #2118 linhas


# In[8]:


dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10] #Somente as 10 primeiras linhas


# In[ ]:




