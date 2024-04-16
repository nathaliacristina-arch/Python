#!/usr/bin/env python
# coding: utf-8

# ## Numpy
# O NumPy é uma biblioteca fundamental para computação científica em Python. Ele fornece suporte para arrays multidimensionais, junto com uma grande coleção de funções matemáticas de alto nível para operar nesses arrays.
# 
# #### Arrays
# Muito melhor que listas, pois é otimizado, pricipalmente para serem usados com matrizes.

# In[ ]:


# Importando o NumPy
import numpy


# In[2]:


# Array criado a partir de uma lista Python
arr1 = numpy.array([10, 21, 32, 43, 48, 15, 76, 57, 89])


# In[3]:


print(arr1)


# In[5]:


type (arr1)


# In[6]:


arr1.shape


#  O NumPy fornece um objeto de matriz N-dimensional (ou ndarray), que é uma grade homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.
# 
# Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois são implementados em Linguagem C e fornecem várias otimizações de desempenho. Além disso, o NumPy permite a fácil leitura e escrita de arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.

# ![image.png](attachment:image.png)
# 
# No caso, temos um Array de 1d com 9 elementos

# ### Arrays

# In[7]:


print (arr1)


# In[11]:


par = ( arr1 % 2 == 0 )
    


# In[15]:


par #imprime uma lista de elementos booleanos


# In[16]:


arr1[par] #imprime somente o índice do verdadeiro, ou seja, somente quando a resposta for true


# In[17]:


# Alterando um elemento do array
arr1[0] = 100


# In[19]:


print (arr1)  #alterou o valor de 10 para 100


# In[ ]:




