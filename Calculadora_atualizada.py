#!/usr/bin/env python
# coding: utf-8

# In[57]:


print ("Selecione o número da operação desejada: \n"
       "1 - Soma \n"
       "2 - Subtração \n"
       "3 - Multiplicacao\n"
       "4 - Divisão \n")


operacao =   (input ("Digite sua opção : \n "))

    


# In[58]:


num1 = int (input ( ("Digite o primeiro numero : " )))


# In[59]:


num2 = int  (input ( ("Digite o segundo numero : " )))


# In[60]:


if operacao == "1":
    resultado = num1 + num2
    print (num1, " + ", num2, " = " , resultado)

elif operacao == "2" :
    resultado = num1 - num2
    print (num1, " - ", num2, " = " , resultado)
    
elif operacao == "3":
    resultado = num1 * num2
    print (num1, " * ", num2, " = " , resultado)

elif operacao == "4":
    resultado = num1 / num2
    print (num1, " / ", num2, " = " , resultado)
    
else:

    print ("Operação Inválida")
    


# In[ ]:




