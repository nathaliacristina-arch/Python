#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ### Strip de Strings em DataFrames do Pandas
# 
# Cuidado para não confundir. Vimos o Split e agora veremos o Strip. São funções diferentes.
# 
# O Strip remove caracteres da string.

# In[4]:


dsa_df.head(3)


# In[5]:


dsa_df['Data_Pedido'].head(3)


# A coluna 'Data_Pedido' é a data de envio do produto no formato YYYY-MM-DD. Imagine que seja necessário deixar o ano apenas com 2 dígitos sem alterar o tipo da variável. Fazemos isso com a função lstrip(), ou seja, left strip.

# In[13]:


# Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
dsa_df['Data_Pedido'].str.lstrip('20') #remove da esquerda, resultado: ano com apenas dois digitos


# In[14]:





# In[15]:


dsa_df['Data_Pedido'].head(3)


# In[ ]:




