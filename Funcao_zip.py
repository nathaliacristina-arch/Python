#!/usr/bin/env python
# coding: utf-8

# ## Função Zip
# 
# A função zip() em Python é uma função que agrupa elementos de múltiplas estruturas de dados iteráveis (como listas, tuplas ou outros objetos iteráveis) juntos em pares. A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como uma lista ou dicionário, se necessário.

# In[1]:


# Criando duas listas
x = [1,2,3]
y = [4,5,6]


# In[2]:


# Unindo as listas. Em Python3 retorna um iterator
zip(x, y)


# In[3]:


# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
list(zip(x,y))


# In[4]:


# Criando 2 dicionários
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}


# In[5]:


# Zip vai unir as chaves
list(zip(d1,d2))


# In[6]:


# Zip pode unir os valores (itens)
list(zip(d1, d2.values()))


# In[ ]:




