#!/usr/bin/env python
# coding: utf-8

# # Pseudo código bubble sort

# Inicie
#  Para cada elemento i no array de tamanho 
#  Para cada elemento j no array de tamanho n - 1
#  Se elemento i for maior que elemento j
#  Troque os elementos i e j
#  Exiba o array ordenado
#    

# # Código em Python

# In[1]:


lista = [6,7,8,3,10,19,4,1,0,61,30,16,17,82,29,34,43,21,11,39,56,67,12]


# In[2]:


def bubble_sort(arr):
   
    n = len(arr)
    for i in range(n): # Para cada elemento i do array


        for j in range(0, n-i-1): # Para cada elemento j do array. Compara o número com o próximo 
 
            if arr[j] > arr[j+1]: # Se elemento i for maior que elemento j


                 arr[j], arr[j+1] = arr[j+1], arr[j] # Troque os elementos i e j
    return arr


# In[3]:


print (bubble_sort(lista))


# In[ ]:




