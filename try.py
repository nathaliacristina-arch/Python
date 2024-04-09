#!/usr/bin/env python
# coding: utf-8

# In[8]:


def usuario ():
    while True:
        try: #tente
            val = int(input("Digite um número: "))
        except: #se não digitar correto
            print ("Você não digitou um número!")
            continue
        else: #somente quando digitar um numero
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val) 


# In[10]:


usuario ()


# In[ ]:




