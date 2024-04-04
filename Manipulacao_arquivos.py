#!/usr/bin/env python
# coding: utf-8

# In[15]:


f = open('arquivos\salarios.csv', 'r')   


# In[16]:


data = f.read()


# In[19]:


rows = data.split ("\n")


# In[20]:


print (rows)


# In[32]:


f = open('arquivos\salarios.csv', 'r')   


# In[33]:


data = f.read()


# In[34]:


rows = data.split ("\n")


# In[35]:


full_data = []


# In[36]:


for row in rows: #para cada linha na minha lista de linhas 
    split_row = row.split (",") #faz split a cada virgula
    full_data.append (split_row)


# In[37]:


print (full_data) #primeira lista, imprime os titulos e assim por diante. Porem, como nome e sobrenome estão separados por vírgula, não seria a melhor solução


# In[38]:


f = open('arquivos\salarios.csv', 'r')   


# In[39]:


data = f.read()


# In[40]:


rows = data.split ("\n")


# In[41]:


full_data = []


# In[42]:


for row in rows: #para cada linha na minha lista de linhas 
    split_row = row.split (",") #faz split a cada virgula
    full_data.append (split_row)


# In[43]:


#Numero de linhas do arquivo
count = 0
for row in full_data:
    count += 1 


# In[44]:


print (count)


# In[45]:


#Numero de colunas do arquivo
first_row = full_data [0]
count1 = 0


# In[46]:


for column in first_row:
    count1 = count1 + 1


# In[47]:


print (count1)


# In[ ]:




