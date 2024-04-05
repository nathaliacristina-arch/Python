#!/usr/bin/env python
# coding: utf-8

# ### Extração de Arquivo da Web

# In[4]:


# Importando o módulo JSON
import json


# In[8]:


# Imprimindo um arquivo JSON copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]


# In[9]:


dados


# In[10]:


print ('Título: ', dados['title'])
print ('URL: ', dados['url'])
print ('Duração: ', dados['duration'])
print ('Número de Visualizações: ', dados['stats_number_of_plays'])


# In[ ]:




