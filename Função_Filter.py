#!/usr/bin/env python
# coding: utf-8

# ## Função Filter
# 
# A função filter() em Python é uma função que filtra elementos de uma estrutura de dados iterável (como uma lista, tupla ou outro objeto iterável) com base em uma determinada condição. A função filter() retorna um objeto filtro, que pode ser convertido em outra estrutura de dados, como uma lista, se necessário.

# In[1]:


# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False


# In[2]:


minha_lista = [1, 2, 3, 4, 5 , 6, 7 , 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# In[3]:


minha_lista


# In[4]:


# A função filter() retorna um iterator
filter(verificaPar, minha_lista)


# In[5]:


lista_filtrada = list
lista_filtrada = (filter(verificaPar, minha_lista))


# In[6]:


lista_filtrada


# In[11]:


list(filter(verificaPar, minha_lista))


# In[15]:


list(filter(lambda x: x%2==0, minha_lista))


# In[16]:


list(filter(lambda num: num > 8, minha_lista))


# In[ ]:




