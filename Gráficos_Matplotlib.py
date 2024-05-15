#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib
# 
# https://matplotlib.org/
# 
# Matplotlib é uma biblioteca de visualização de dados em Python amplamente utilizada para criar gráficos e visualizações de alta qualidade em diversas áreas, como ciência de dados, engenharia, finanças, estatística, entre outras. É uma biblioteca extremamente poderosa, flexível e personalizável, que permite a criação de gráficos em 2D e 3D, histogramas, diagramas de dispersão, gráficos de linhas, entre outros.
# 
# O Matplotlib oferece uma grande variedade de estilos de plotagem, tipos de gráficos e configurações de plotagem para personalização de gráficos. Ele é compatível com vários formatos de arquivos de imagem, como PNG, PDF, SVG, entre outros, permitindo a geração de imagens de alta qualidade para uso em publicações e apresentações.

# In[1]:


import matplotlib as mpl


# ## Construindo Plots
# 
# Plot é uma representação gráfica de dados em uma figura. Em outras palavras, é um gráfico que mostra a relação entre duas ou mais variáveis. Um plot pode ser criado usando uma biblioteca de visualização de dados, como o Matplotlib em Python.

# In[6]:


# O matplotlib.pyplot é uma coleção de funções e estilos do Matplotlib 
import matplotlib.pyplot as plt #construção e personalização de gráficos #operador mágico, para plotar o grafico nessa mesma página
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


# O método plot() define os eixos do gráfico
plt.plot([1, 3, 5], [2, 4, 7])
plt.show()


# In[8]:


x = [2, 3, 5]
y = [3, 5, 7]


# In[9]:


plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Gráfico com Matplotlib')
plt.show()


# In[11]:


x2 = [1, 2, 3]
y2 = [11, 12, 15]


# In[12]:


plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend()
plt.show()


# ## Gráfico de Barras
# 
# Gráfico de barras é um tipo de plotagem usado para representar dados categóricos com barras retangulares. Cada barra representa uma categoria e a altura da barra representa a quantidade ou frequência da categoria.
# 
# O eixo horizontal do gráfico de barras mostra as categorias e o eixo vertical mostra a escala de medida dos dados. As barras podem ser vertical ou horizontal, dependendo da preferência do usuário.

# In[13]:


x1 = [2,4,6,8,10]
y1 = [6,7,8,2,4]


# In[14]:


plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()


# In[15]:


plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.bar(x2, y2, label = 'Listas2', color = 'red')
plt.legend()
plt.show()


# In[16]:


idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]


# In[17]:


ids = [x for x in range(len(idades))]


# In[18]:


print(ids)


# In[19]:


plt.bar(ids, idades)
plt.show()


# In[21]:


bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]


# In[22]:


plt.hist(idades, bins, histtype = 'stepfilled', rwidth = 0.8)
plt.show()


# ## Gráfico de Dispersão
# 
# Gráfico de dispersão, também conhecido como gráfico de pontos, é um tipo de plotagem utilizado para representar a relação entre duas variáveis contínuas. Cada ponto no gráfico de dispersão representa um par de valores das duas variáveis, onde uma variável é plotada no eixo horizontal e outra no eixo vertical.

# In[23]:


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]


# In[30]:


plt.scatter(x, y, label = 'Pontos', color = 'r', marker = '*')
plt.legend()
plt.show()


# ### Gráfico de Área Empilhada
# 
# Stack plots, também conhecidos como gráficos de área empilhada, são um tipo de plotagem usados para visualizar a mudança relativa de diversas variáveis ao longo do tempo. Eles consistem em várias áreas coloridas empilhadas umas sobre as outras, onde a altura de cada área representa a magnitude da variável correspondente e a largura representa a escala de tempo.

# In[31]:


dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]


# In[32]:


plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()


# ## Gráfico de Pizza
# 
# Gráfico de Pizza (Pie Plot), também conhecido como gráfico de setores, é um tipo de plotagem que representa a composição de uma variável categórica em relação ao todo. Ele é representado por um círculo dividido em fatias que representam as proporções relativas das categorias.
# 
# Cada fatia do gráfico de pizza corresponde a uma categoria e sua área é proporcional à porcentagem que a categoria representa do todo. A categoria mais representativa é geralmente posicionada na parte superior do círculo, enquanto as outras fatias são posicionadas em sentido horário.

# In[33]:


fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']


# In[34]:


plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0,0.2,0,0))
plt.show()


# ## Criando Gráficos Customizados com Pylab
# 
# Pylab é um módulo fornecido pela biblioteca Matplotlib que combina a funcionalidade do pacote NumPy com a funcionalidade do pacote pyplot. Ele fornece um ambiente de plotagem interativo, permitindo que os usuários criem rapidamente gráficos e visualizações de dados.
# 

# In[35]:


# O Pylab combina funcionalidades do pyplot com funcionalidades do Numpy
from pylab import *
get_ipython().run_line_magic('matplotlib', 'inline')


# In[36]:


# Gráfico de linha

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Define a escala dos eixos
axes = fig.add_axes([0, 0, 0.8, 0.8])

# Cria o plot
axes.plot(x, y, 'r')

# Labels e título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha');


# In[39]:


# Gráficos de linha com 2 figuras

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Cria os eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # eixos da figura secundária

# Figura principal
axes1.plot(x, y, 'g')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y, x, 'r')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária');


# In[41]:


# Gráficos de linha em Paralelo

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Divide a área de plotagem em dois subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)

# Loop pelos eixos para criar cada plot
for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')
    
# Ajusta o layout
fig.tight_layout()


# In[44]:


# Gráficos de linha com diferentes escalas

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10,4))
      
# Cria o plot1
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title("Escala Padrão")

# Cria o plot2
axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale("log") #muda-se a escala dos dados para log
axes[1].set_title("Escala Logaritmica")


# In[45]:


# Grid

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10,3))

# Grid padrão
axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

# Grid customizado
axes[1].plot(x, x**2, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8) #dashed=pontilhada


# In[46]:


# Diferentes estilos de Plots

# Dados
xx = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

# Subplots
fig, axes = plt.subplots(1, 4, figsize = (12,3))

# Plot 1
axes[0].scatter(xx, xx + 0.25 * randn(len(xx)), color = "black")
axes[0].set_title("scatter")

# Plot 2
axes[1].step(n, n ** 2, lw = 2, color = "blue")
axes[1].set_title("step")

# Plot 3
axes[2].bar(n, n ** 2, align = "center", width = 0.5, alpha = 0.5, color = "magenta")
axes[2].set_title("bar")

# Plot 4
axes[3].fill_between(x, x ** 2, x ** 3, alpha = 0.5, color = "green");
axes[3].set_title("fill_between");


# ### Histogramas
# 
# Histogramas são um tipo de plotagem utilizado para visualizar a distribuição de uma variável contínua. Eles são compostos por barras retangulares adjacentes, onde a área de cada barra é proporcional à frequência de observações de dados que caem em uma faixa específica de valores.
# 
# No histograma, a variável contínua é dividida em faixas de valores, conhecidas como intervalos de classe. O eixo horizontal representa os intervalos de classe, enquanto o eixo vertical representa a frequência de observações de dados que caem em cada intervalo de classe. Os intervalos de classe devem ser escolhidos de forma apropriada para a distribuição dos dados e a escala dos eixos deve ser definida adequadamente.

# In[48]:


# Histogramas

# Dados
n = np.random.randn(100000)

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (12,4)) #1= linhas, 2= colunas

# Plot 1
axes[0].hist(n)
axes[0].set_title("Histograma Padrão")
axes[0].set_xlim((min(n), max(n))) #limites

# Plot 2
axes[1].hist(n, cumulative = True, bins = 50 , color = 'red')
axes[1].set_title("Histograma Cumulativo")
axes[1].set_xlim((min(n), max(n)));


# ### Gráfico 3D

# In[49]:


from mpl_toolkits.mplot3d.axes3d import Axes3D


# In[50]:


# Dados
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

# Função para um mapa de cores
def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

# Mais dados
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T


# In[51]:


# Cria a figura
fig = plt.figure(figsize = (14,6))

# Adiciona o subplot 1 com projeção 3d
ax = fig.add_subplot(1, 2, 1, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# Adiciona o subplot 2 com projeção 3d
ax = fig.add_subplot(1, 2, 2, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Cria a barra de cores como legenda
cb = fig.colorbar(p, shrink=0.5)


# In[53]:


# Wire frame

# Cria a figura
fig = plt.figure(figsize=(8,6))

# Subplot
ax = fig.add_subplot(1, 1, 1, projection = '3d')

# Wire frame
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)


# In[ ]:




