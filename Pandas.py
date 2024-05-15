#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'], 
         'Ano': [2004, 2005, 2006, 2007, 2008], 
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}


# In[2]:


# Importa a função DataFrame do Pandas
from pandas import DataFrame


# In[3]:


# Converte o dicionário em um dataframe
df = DataFrame(dados)


# In[4]:


# Visualiza as 5 primeiras linhas
df.head()


# In[5]:


# Reorganizando as colunas
DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])


# In[6]:


# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, 
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'], 
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])


# In[7]:


df2


# In[ ]:




