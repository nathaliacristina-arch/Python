#!/usr/bin/env python
# coding: utf-8

# # Crie uma lista com os números entre 1 e 100 e então imprima os números pares, mas somente se o números for divisivel por 4, usando  list comprehension

# In[1]:


# Criar uma lista de números de 1 a 100
numeros = list(range(1, 101))


# In[2]:


type (numeros)


# In[3]:


# Filtrar os números pares que são divisíveis por 4
numeros_divisiveis_por_4 = [num for num in numeros if num % 2 == 0 and num % 4 == 0]
print(numeros_divisiveis_por_4)


# In[4]:


type (numeros_divisiveis_por_4)


# In[ ]:




