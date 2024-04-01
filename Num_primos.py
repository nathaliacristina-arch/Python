#!/usr/bin/env python
# coding: utf-8

# # While e For Juntos
# 
# Vamos encontrar números primos em uma coleção de números usando loop While e For juntos.
# Um número primo é um número natural maior do que 1 que é divisível apenas por 1 e por ele mesmo. Isso significa que não há nenhum outro número inteiro que possa dividir o número primo sem deixar resto. Por exemplo, o número 2 é primo, pois é divisível apenas por 1 e 2. O número 4 não é primo, pois é divisível por 2.
# 
# # pseudocódigo
# 
# Inicialize uma lista vazia para armazenar os números primos
# Para cada número N entre 2 e 30
# Inicialize uma variável eh_primo como verdadeira
# Para cada número i entre 2 e N/2:
# Se N é divisível por i, então:
# Altere a variável eh_primo para falso
# Pare de verificar os outros números
# Se a variável eh_primo ainda é verdadeira, adicione N à lista de números primos\
# Imprima a lista de números primos

# In[5]:


get_ipython().run_cell_magic('time', '', '   \n# Encontrando números primos entre 2 e 30 usando loop for e while\n\n# Variável para armazenar números primos\nprimos = []\n\n# Loop for para percorrer números de 2 a 30\nfor num in range(2, 31):\n   \n   # Variável de controle\\n",\n   eh_primo = True\n\n   # Loop while para verificar se o número é primo\\n",\n   i = 2\n   while i <= num // 2:\n       if num % i == 0:\n           eh_primo = False\n           break\n       i += 1\n\n# Adicionando o número primo na lista\n   if eh_primo:\n       primos.append(num)\n       \n# Imprimindo a lista de números primos\nprint(primos)\n  ')


# In[4]:


get_ipython().run_cell_magic('time', '', '    \n# Encontrando números primos entre 2 e 30 usando loop for e while (outro exemplo)\n# Loop for para percorrer números de 2 a 30\\n",\nfor i in range(2,31):\n        # Variável de controle\n        j = 2\n        # Contador\n        valor = 0\n    \n        # Loop while para verificar se o número é primo\\n",\n        while j < i:\n            if i % j == 0:\n                valor = 1\n                j = j + 1\n            else:\n                j = j + 1\n    \n        if valor == 0:\n            print(str(i) + " é um número primo")\n            valor = 0\n        else:\n            valor = 0')


# In[ ]:




