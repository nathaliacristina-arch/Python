#!/usr/bin/env python
# coding: utf-8

# ## Statistical Data Visualization com Seaborn 

# In[1]:


# Imports
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import seaborn as sea
sea.__version__


# ## Criando Gráficos com Seaborn

# In[3]:


# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset("tips")


# In[4]:


dados.head()


# In[5]:


# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg') # reg=linha de regressão


# In[6]:


# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")


# In[7]:


# Construindo um dataframe com Pandas
df = pd.DataFrame()


# In[8]:


# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)


# In[9]:


df.shape


# In[10]:


df.head()


# In[11]:


# lmplot
sea.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)


# In[12]:


# kdeplot
sea.kdeplot(df.idade)


# In[13]:


# kdeplot
sea.kdeplot(df.peso)


# In[14]:


# distplot
sea.distplot(df.peso)


# In[20]:


# Histograma
plt.hist(df.idade, alpha = .3)
sea.rugplot(df.idade) #rugas/traços quie indicam as idades


# In[21]:


# Box Plot
sea.boxplot(df.idade, color = 'm') #segundo quartil é a linha do meio. A ,linha de cima=primeiro quartil e o de baixo=terceiro quartil


# In[17]:


# Box Plot
sea.boxplot(df.peso, color = 'y')


# In[18]:


# Violin Plot
sea.violinplot(df.idade, color = 'g')


# In[19]:


# Clustermap
sea.clustermap(df)


# In[26]:


# Valores randômicos
np.random.seed(42)
n = 1000
pct_smokers = 0.2 #2% = fumantes

# Variáveis
flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_fumante': flag_fumante})  #Dicionario

# Cria os dados para a variável flag_fumante
dados['flag_fumante'] = dados['flag_fumante'].map({True: 'Fumante', False: 'Não Fumante'})


# In[23]:


dados.shape


# In[27]:


dados.head()


# In[24]:


# Style
sea.set(style = "ticks")

# lmplot
sea.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_fumante', #legenda de acordo com flag_fumante
           palette = ['tab:blue', 'tab:orange'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de Fumantes e Não Fumantes')

# Remove as bordas
sea.despine()

# Show
plt.show()


# In[ ]:




