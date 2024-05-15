#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# In[4]:


dsa_df['ID_Pedido'].head()


# Este é o formato dos dados da coluna "ID_Pedido":
# 
# CA-2016-152156
# US-2015-108966
# Temos o país, o ano e o id do pedido. Vamos dividir essa coluna e extrair o ano para gravar em uma nova coluna:

# In[5]:


# Split da coluna pelo caracter '-'
dsa_df['ID_Pedido'].str.split('-')


# In[8]:


# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1] #Cria a coluna ano e coloca os dados que foi buscado atraves do split


# In[7]:


# Então conferimos a nova coluna criada
dsa_df.head()


# In[ ]:




