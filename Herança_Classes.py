#!/usr/bin/env python
# coding: utf-8

# ##  Herança de Classes em Python
# 
# Em Programação Orientada a Objetos (POO), a herança é um conceito que permite criar novas classes a partir de outras classes existentes, aproveitando os atributos e métodos da classe original e adicionando novos atributos e métodos específicos. 
# 
# A classe original é chamada de classe mãe ou superclasse e a nova classe criada é chamada de classe filha ou subclasse.

# In[1]:


# Criando a classe Animal - Super-classe
class Animal:
    
    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")
        
    def emitir_som(self):
        pass


# In[2]:


# Criando a classe Cachorro - Sub-classe
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro criado.")
    
    def emitir_som(self):
        print("Au au!")


# In[3]:


# Criando a classe Gato - Sub-classe
class Gato(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")
    
    def emitir_som(self):
        print("Miau!")


# In[4]:


# Criando um objeto (Instanciando a classe)
rex = Cachorro()


# In[5]:


rex.emitir_som() 


# In[6]:


# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()


# In[7]:


# Executando o método da classe Animal (super-classe)
rex.comer()


# In[ ]:




