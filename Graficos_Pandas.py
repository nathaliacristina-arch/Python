#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Primeiro importamos um dataset
dsa_df = pd.read_csv("dataset.csv")


# In[3]:


dsa_df.head()


# ### Construção de Gráficos a Partir de DataFrames do Pandas
# 
# Vimos até aqui diversas funcionalidades do Pandas que tornam o processo de manipulação de dados realmente simples. E para concluir este capítulo vamos estudar as opções que o Pandas oferece para criação de gráficos diretamente a partir de dataframes, sem a necessidade de usar qualquer outra biblioteca.

# In[4]:


# Instala a versão exata do Scikit-learn
get_ipython().system('pip install -q scikit-learn==1.2.1')


# In[5]:


import sklearn
sklearn.__version__


# In[6]:


# Vamos começar importando o dataset iris do Scikit-learn
from sklearn.datasets import load_iris
data = load_iris()


# In[7]:


# E então carregamos o dataset iris como dataframe do Pandas, medidas de especies de plantas
import pandas as pd
df = pd.DataFrame(data['data'], columns = data['feature_names'])
df['species'] = data['target']
df.head()


# In[8]:


# Para criar um gráfico de linhas com todas as variáveis do dataframe, basta fazer isso:
df.plot()


# In[9]:


# Que tal um scatter plot com duas variáveis? 
df.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')


# In[10]:


# E mesmo gráficos mais complexos, como um gráfico de área, pode ser criado:
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area()


# In[11]:


# Calculamos a média das colunas agrupando pela coluna species e criamos um gráfico de barras com o resultado
df.groupby('species').mean().plot.bar()


# In[12]:


# Ou então, fazemos a contagem de classes da coluna species e plotamos em um gráfico de pizza
df.groupby('species').count().plot.pie(y = 'sepal length (cm)')


# In[13]:


# Gráfico KDE (Kernel Density Function) para cada variável do dataframe
df.plot.kde(subplots = True, figsize = (8,8))


# In[14]:


# Boxplot de cada variável numérica
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.box(figsize = (8,8))


# In[ ]:




