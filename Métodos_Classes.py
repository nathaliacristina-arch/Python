#!/usr/bin/env python
# coding: utf-8

# ## Métodos
# 
# Em Python, os métodos de classes são funções definidas dentro de uma classe, que realizam operações específicas em objetos criados a partir dessa classe. Os métodos de classes são usados para implementar o comportamento dos objetos que pertencem a essa classe.
# 
# Assim como as funções em Python, os métodos de classes podem receber argumentos e retornar valores. No entanto, diferentemente das funções normais, os métodos de classes sempre incluem o parâmetro self como o primeiro argumento, que é usado para se referir ao objeto atual da classe.

# In[9]:


# Criando uma classe chamada Circulo
class Circulo():
    
    # O valor de pi é ** constante **, assim não preciso colocar ele dentro das funções da classe
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio = 5):
        self.raio = raio 

    # Esse método calcula a área. 
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio


# In[10]:


# Criando o objeto circ, uma instância da classe Circulo()
circ = Circulo()


# In[11]:


# Executando um método da classe Circulo
circ.getRaio()


# In[12]:


# Criando outro objeto chamado circ1. Uma instância da classe Circulo()
# Agora sobrescrevendo o valor do atributo
circ1 = Circulo(7)


# In[13]:


# Executando um método da classe Circulo
circ1.getRaio()


# In[14]:


# Imprimindo a area
print('Área igual a:', circ.area())


# In[15]:


# Gerando um novo valor para o raio do círculo
circ.setRaio(3)


# In[16]:


# Imprimindo o novo raio
print ('Novo raio igual a:', circ.getRaio())

