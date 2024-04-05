#!/usr/bin/env python
# coding: utf-8

# ## Função Reduce
# A função reduce() em Python é uma função da biblioteca functools que aplica uma determinada função binária a pares consecutivos de elementos em uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável), reduzindo-a a um único valor.

# In[2]:


# Importando a função reduce do módulo functools
from functools import reduce


# In[3]:


from IPython.display import Image
Image('arquivos/reduce.png')


# In[5]:


# Criando uma lista
lst = [47, 11, 42, 13]


# ### Usando LAMBDA

# In[7]:


# Usando a função reduce() com lambda
reduce(lambda x,y: x+y, lst)


# In[8]:


# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b


# In[9]:


reduce(max_find2, lst)


# In[ ]:




