#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Criando a classe Livro com parâmetros no método construtor
class Livro():
    
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")
        
    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo, isbn))


# In[2]:


# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)


# In[3]:


Livro2.titulo


# In[4]:


# Método do objeto Livro2
Livro2.imprime("O Poder do Hábito", 77886611)


# In[5]:


# Criando o objeto Livro2 que é uma instância da classe Livro
Livro3 = Livro("A arte de ligar o foda-se", 12903451)


# In[6]:


Livro3.titulo


# In[8]:


Livro3.imprime ("A arte de ligar o foda-se", 12903451)


# In[ ]:




