#!/usr/bin/env python
# coding: utf-8

#  Para calcular a área de um paralelograma, podemos seguir os seguintes passos:
#  
# 1-  Declare as variáveis  comprimento e altura.
# 2-  Peça ao usuário para fornecer os valores de comprimento e altura.
# 3- Calcule a área multiplicando comprimento pela altura.
# 4- Armazene o resultado na variável "área".
# 5- Imprima o valor da variável "área".
# 

# Aqui está um exemplo de pseudocódigo que implementa esses passos:
#  Declare comprimento, altura, area
#  Obtenha comprimento do usuário
#  Obtenha altura do usuário
#  area <- comprimento * altura
#  Imprima "A área do paralelograma é:" + area

# In[1]:


print ("Bem vindo ao calculador de área de Paralelogramo")


# In[2]:


Base = float (input("Insira o comprimento da base: "))


# In[3]:


Altura = float (input("Insira a altura: "))


# In[4]:


Area = Base + Altura


# In[5]:


print (" A area do paralelogramo é: ", Area)


# # pseudo código 2
# 

#  Exiba "Bem-vindo à Calculadora"
#     1- Peça para o usuário inserir o primeiro número
#     2- Armazene o primeiro número em uma variáve
#     3- Peça para o usuário inserir o segundo número
#     4- Armazene o segundo número em uma variável
#     5- Peça para o usuário selecionar uma operação (+, -, *, /)
#     6- Armazene a operação em uma variável
#     7- Utilize a operação selecionada e os números armazenados para realizar o cálculo
#     8- Exiba o resultado,
# 
# 

# In[18]:


print ("Bem-vindo a calculadora")


# In[19]:


num1 = float (input ("Insira o primeiro número: "))


# In[20]:


num2 = float (input ("Insira o primeiro número: "))


# In[21]:


operacao = input ("Selecione uma operação ")


# In[24]:


if operacao == "+":
    resultado = num1 + num2
    print("O resutado é: " ,resultado)
    
elif  operacao == "-" :
    resultado = num1 - num2
    print("O resutado é: " ,resultado)
     
elif  operacao == "*":
    resultado = num1 * num2
    print("O resutado é: " ,resultado)
    
elif  operacao == "/":
    resultado = num1 / num2
    print("O resutado énvá: " ,resultado)
    
else: 
    print ("Operação inválida ")


# In[ ]:




