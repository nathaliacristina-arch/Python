#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Loop em lista de listas (matrizes) para encontrar o maior número\n",

matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0 #Maior numero começa em zero

# Loop externo, percorre toda a Matriz
for linha in matriz:
    
# Loop interno, percorre toda a linha 
    for num in linha:
# Condicional
         if num > maior_numero: 
            maior_numero = num
print("Maior número:  ", maior_numero)


# In[ ]:




