#!/usr/bin/env python
# coding: utf-8

# # Crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o números for divisivel por 4

# In[1]:


# Criar uma lista de números de 1 a 100
numeros = list(range(1, 101))


# In[2]:


type (numeros)


# In[3]:



for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)


# In[ ]:




