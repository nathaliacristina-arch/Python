#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math


# In[9]:


# Verificando se um número é primo
def numPrimo(num):
   if (num % 2) == 0 and num > 2: #Número par, maior que 2?
       return "Este número não é primo"
   
   for i in range(3, int(math.sqrt(num)) + 1, 2) #Percorre do número 3, até a raiz quadrada do número, de dois em dois
           if (num % i) == 0:         # Verifica se o número é divisível por algum dos números ímpares (além de 2)
               return "Este número não é primo"
           
   return "Este número é primo"


# In[10]:


numPrimo (541)


# In[11]:


numPrimo (2)


# In[12]:


numPrimo (17)


# In[13]:


numPrimo (18)


# In[ ]:




