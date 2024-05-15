#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


import pandas as pd


# ## Conectando no Banco de Dados com Linguagem Python
# 

# In[3]:


# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db') #arquivo precisa estar na mesma pasta do jupyter notebook


# In[4]:


# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()


# In[5]:


# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';""" #query=consulta


# In[6]:


# Executa a query
cursor.execute(sql_query)


# In[7]:


# Visualiza o resultado
print(cursor.fetchall())


# In[8]:


# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'


# In[9]:


# Executa a query no banco de dados
cursor.execute(query1)


# In[10]:


# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]


# In[11]:


# Visualiza o resultado
print(nomes_colunas)


# In[12]:


# Retorna os dados da execução da query
dados = cursor.fetchall()


# In[13]:


# Visualiza os dados
dados


# ## Aplicando Linguagem SQL Direto no Banco de Dados com Linguagem Python

# In[18]:


# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'


# In[19]:


# Executa a query no banco de dados
cursor.execute(query2)


# In[20]:


# Visualiza o resultado - média dos produtos vendidos
print(cursor.fetchall())


# In[24]:


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto' #média por produto vendido


# In[25]:


# Executa a query no banco de dados
cursor.execute(query3)


# In[26]:


# Visualiza o resultado
cursor.fetchall()


# In[ ]:





# In[72]:


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto"""

#SOMENTE PARA OS PRODUTOS COM VALOR MAIOR QUE 199


# In[73]:


# Executa a query no banco de dados
cursor.execute(query4)


# In[64]:


# Visualiza o resultado
cursor.fetchall()


# In[65]:


cursor.close()
con.close()


# In[66]:


# Esta query está ERRADA!
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 and AVG(Unidades_Vendidas) > 10
            GROUP BY Nome_Produto """


# In[67]:


# Executa a query no banco de dados
# cursor.execute(query5)


# In[68]:


#Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""


# In[69]:


# Executa a query no banco de dados
cursor.execute(query5)


# In[70]:


# Visualiza o resultado
cursor.fetchall()


# In[49]:


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# ## Aplicando Linguagem SQL na Sintaxe do Pandas com Linguagem Python

# In[74]:


# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')


# In[75]:


# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()


# In[76]:


# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'


# In[77]:


# Executa a query no banco de dados
cursor.execute(query)


# In[78]:


# Retorna os dados da execução da query
dados = cursor.fetchall()


# In[79]:


dados


# In[80]:


type(dados)


# In[81]:


# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido', 
                                    'ID_Cliente', 
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])


# In[82]:


# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# In[83]:


# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()


# In[84]:


type(media_unidades_vendidas)


# In[85]:


print(media_unidades_vendidas)


# In[86]:


# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# In[87]:


# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))


# In[88]:


# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# In[89]:


# Alternativa A
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)


# In[90]:


# Alternativa B
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')                               .filter(lambda x: x['Unidades_Vendidas'].mean() > 10)                               .groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# ## Sintaxe SQL x Sintaxe Pandas
# 

# In[91]:


# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas) 
            FROM tb_vendas_dsa 
            WHERE Valor_Unitario > 199 
            GROUP BY Nome_Produto 
            HAVING AVG(Unidades_Vendidas) > 10"""


# In[92]:


# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')                               .filter(lambda x: x['Unidades_Vendidas'].mean() > 10)                               .groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# In[ ]:




