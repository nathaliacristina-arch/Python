#!/usr/bin/env python
# coding: utf-8

# # Pseudo código calculadora simples

# Exiba "Bem-vindo à Calculadora"
#     1- Peça para o usuário inserir o primeiro número
#     2- Armazene o primeiro número em uma variáve
#     3- Peça para o usuário inserir o segundo número
#     4- Armazene o segundo número em uma variável
#     5- Peça para o usuário selecionar uma operação (+, -, *, /)
#     6- Armazene a operação em uma variável
#     7- Utilize a operação selecionada e os números armazenados para realizar o cálculo
#     8- Exiba o resultado

# # Código em Python

# In[ ]:


print ("Bem-vindo a calculadora")


# In[ ]:


num1 = float (input ("Insira o primeiro número: "))


# In[ ]:


num2 = float (input ("Insira o primeiro número: "))


# In[ ]:


operacao = input ("Selecione uma operação ")


# In[ ]:


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





# In[ ]:





# In[ ]:




