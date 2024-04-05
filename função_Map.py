#!/usr/bin/env python
# coding: utf-8

# ## Função Map
# 
# A função map() em Python é uma função de ordem superior que aplica uma função a todos os itens de um iterável (como uma lista, tupla, etc.) e retorna um iterador que produz os resultados

# #### Função Python que retorna a temperatura convertida
# 

# In[9]:



# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return (float(5)/9)*(T-32)


# In[10]:


# Criando uma lista
temperaturas = [0, 22.5, 40, 100]


# In[11]:


# Aplicando a função a cada elemento da lista de temperaturas. 
# Em Python 3, a funçãp map() retornar um iterator
map(fahrenheit, temperaturas)


# In[12]:


# Função map() retornando a lista de temperaturas convertidas em Fahrenheit
list(map(fahrenheit, temperaturas))


# In[13]:


# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)


# In[ ]:




