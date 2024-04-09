#!/usr/bin/env python
# coding: utf-8

# ## Função Enumerate
# 
# A função enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados (como uma lista, tupla ou outro objeto iterável). A função enumerate() retorna um objeto enumerado, que pode ser usado em loops para percorrer a estrutura de dados e acessar o contador e o valor de cada elemento.

# In[5]:


# Criando uma lista
seq = ['a','b','c', 'd', 'e', 'f', 'g', 'h', 'i']


# In[6]:


enumerate(seq)


# In[7]:


list(enumerate(seq))


# In[8]:


# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print (indice, valor)


# In[10]:


for indice, valor in enumerate(seq):
    if indice >= 5:
        break
    else:
        print (valor)


# enumera também letras

# In[14]:


for i, item in enumerate('Nathalia Cristina'):
    print(i, item)


# In[ ]:




