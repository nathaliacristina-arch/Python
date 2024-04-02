#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Funções com número variável de argumentos

def printVarInfo( arg1, *vartuple ): #vartuple com * aceita qualquer valor de argumentos. Assim, no caso, aceitaria o elementos, 1 ou 2 ou 3...
    
# Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)

# Imprimindo o valor do segundo argumento 
    for item in vartuple:
            print ("O parâmetro passado foi: ", item) #Se houver mais de um argumento, entra nesse loop, e a cada elemento ele o imprime 
    return;
   


# In[12]:


printVarInfo(10)


# In[13]:


printVarInfo('Chocolate', 'Morango')


# In[14]:


printVarInfo ("Maria", "João", "José")

