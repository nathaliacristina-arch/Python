#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Loops aninhados\n

lista1 = [0,1,2,3,4]
lista2 = [1,2,3]

# Loop externo
for elemento_lista1 in lista1:
    
    # Loop interno\n",
    for elemento_lista2 in lista2:
        print('\\n', elemento_lista1 * elemento_lista2)
    
    print('----')
   


# In[ ]:




