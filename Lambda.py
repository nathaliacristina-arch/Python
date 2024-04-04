#!/usr/bin/env python
# coding: utf-8

# # Função Lambda
# 
# Uma função lambda em Python é uma função anônima, o que significa que é uma função sem nome.
# Ela é definida usando a palavra-chave lambda, seguida por uma lista de argumentos, um sinal de dois pontos (:)
# e uma expressão que é avaliada e retornada como resultado da função.

# In[7]:


potencia = lambda num: num ** 2 


# In[8]:


potencia (5)


# In[9]:


par = lambda x : x % 2 == 0


# In[10]:


par (3)


# In[11]:


par (5)


# In[12]:


par (4)

