#!/usr/bin/env python
# coding: utf-8

# ## Expressões Regulares
# 
# Expressões regulares são padrões usados para combinar ou encontrar ocorrências de sequências de caracteres em uma string. Em Python, expressões regulares são geralmente usadas para manipular strings e realizar tarefas como validação de entrada de dados, extração de informações de strings e substituição de texto.

# In[1]:


# Variável do tipo string
musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''


# In[6]:


print (musica)


# In[7]:


# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.


# In[8]:


import re


# In[9]:


# Expressão regular para contar quantas vezes o caracter "a" aparece no texto
resultado = len(re.findall("a", musica))


# In[29]:


print (" o caracter a aparece em todo o texto da música: " , resultado , "vezes")


# In[11]:


# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.


# In[25]:


# Expressão regular para contar quantas vezes a palavra "tempo" aparece no texto
resultado = len(re.findall("tempo", musica))


# In[27]:


print ("A palavra tempo aparece na música: " , resultado , "vezes")


# In[14]:


# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.


# In[20]:


resultado = re.findall(r'\b\w+!', musica)


# In[23]:


print ("As palavras que são seguidas por exclamação são: " , resultado)


# In[30]:


# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.


# In[33]:


resultado = re.findall(r"esse\s(\w+)\samargo", musica)


# In[34]:


resultado


# In[ ]:


# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.


# In[35]:


resultado = re.findall(r"(\w+)[\u00C0-\u017F]+", musica)
print("Palavras com acento, sem o acento:", resultado) #anteriores a letra com acento


# In[36]:


resultado5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", resultado5) #letras até o acento + acento


# In[ ]:




