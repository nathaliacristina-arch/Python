#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Criando uma classe
class Funcionarios:
    
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo) #imprime uma mensagem com várioas strings 


# In[6]:


# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Nathalia", 5000, "Cientista de Dados")


# In[7]:


# Usando o método da classe
Func1.listFunc()


# In[8]:


#No Func 1 tem o atributo nome?
hasattr(Func1, "nome")


# In[11]:


#mude o valor do atributo salario
setattr(Func1, "salario", 4500)


# In[12]:


#Imprime o atributo salario
getattr(Func1, "salario")


# In[ ]:




