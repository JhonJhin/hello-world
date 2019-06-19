#!/usr/bin/env python
# coding: utf-8

# # Teste de Objetos e Estrutura de Dados

# ## Teste seu conhecimento.
# 
# ** Responda as seguintes questões **

# # Escreva uma breve descrição de todos os seguintes tipos de objetos e estruturas de dados sobre os quais aprendemos:

# Números: tipo float (3.4, 4.1, 3.456) tipo int (1,2,3,4,5). Escrevem-se sem aspas.
# 
# Strings: Cordas que o kernel visualiza elemento por elemeto, usa-se indexação. Escrevem-se com aspas ou com a função print('String') depende o que se quer apresentar e como.
# 
# Listas: Listas contem elementos de diversos tipos dentro da mesma. Como tuplas, strings, números, outras listas e dicionários. São criadas com [colchetes]. Podem se concatenar listas.
# 
# Tuplas: Tuplas são como as listas, só que criadas usando (parênteses) e são imutáveis.
# 
# Dicionários: Criados usando {chaves}, nele cada 'key' - corresponde a uma valor 'value' .  'key':'Keyvalue' . 

# # Números
# 
# # Escreva uma equação que use multiplicação, divisão, expoente, adição e subtração igual a 100,25.
# 
# Dica: isso é apenas para testar sua memória dos comandos aritméticos básicos, trabalhar para trás a partir de 100.25

# In[3]:


32.75 * (1 + 2) - 2 + 2 ** 2 / 1


# # Responda estas 3 perguntas sem digitar o código. Em seguida, digite o código para verificar sua resposta.
# 
#      Qual é o valor da expressão 4 * (6 + 5)
#     
#      Qual é o valor da expressão 4 * 6 + 5?
#     
#      Qual é o valor da expressão 4 + 6 * 5?

# 1) 44
# 2) 29
# 3) 34

# In[1]:


4 * (6+5)


# In[2]:


4 * 6 + 5


# In[3]:


4 + 6 * 5


# Qual é o * tipo * do resultado da expressão 3 + 1.5 + 4?

# In[4]:


3 + 1.5 + 4


# In[5]:


type(8.5)


# O que você usaria para encontrar a raiz quadrada de um número, bem como seu quadrado?

# In[6]:


16**0.5


# ## Strings

# Dada a string 'hello', dê um comando de índice que retorna 'e'. Use o código abaixo:

# In[8]:


s = 'hello'


# Código aqui 
s[1]


# Inverta a string 'hello' usando indexação:

# In[10]:


s ='hello'


# Código aqui
s[::-1]


# Dado o exemplo de linha, dê dois métodos para produzir a letra 'o' usando a indexação.

# In[7]:


s ='hello'


# Código aqui
#s[-1]
s[4]


# ## Listas

# Crie esta lista [0,0,0] duas formas diferentes.

# In[13]:


s = [0,0,0]


# In[8]:


s = []


# In[16]:


s.append(0)


# In[20]:


s.remove(2)


# In[21]:


s


# In[22]:


[0]*3


# Altere o 'hello' da lista para 'goodbye'

# In[20]:


l = [1,2,[3,4,'hello']]


# In[26]:


l[2][2] = 'goodbye'


# In[27]:


l


# Ordene a lista:

# In[28]:


l = [5,3,4,6,1]
l.sort()


# In[29]:


l


# ## Dicionários

# Usando chaves e indexação, pegue o 'hello' dos seguintes dicionários:

# In[30]:


d = {'simple_key':'hello'}
d['simple_key']


# In[31]:


d = {'k1':{'k2':'hello'}}
d['k1']['k2']


# In[46]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1][0]


# In[10]:


# Esse é chato...
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2][0]


# # Você pode classificar um dicionário? Por que ou por que não?
# 
# Não pode-se pois dicionários são 'mapeamentos' e não uma 'sequência'.

# ## Tuplas

# # Qual é a principal diferença entre as tuplas e as listas?

# Listas são mais maleáveis, ao contrarío das tuplas que são imutáveis!

# # Como você cria uma tupla?

# Crio usando parentesês.

# ## Conjuntos 

# # O que é único em um conjunto?

# ELes não permitem itens duplicados.

# # Use um conjunto para encontrar os valores exclusivos da lista abaixo:

# In[40]:


a = list(set(l))


# In[1]:


l = [1,22,3,3,4,5,7,22,33,44,90]
list(set(l)) #transformando a lista em um conjunto para retirar itens repetidos e convertendo novamente para uma lista.


# In[42]:


a


# ## Booleans

# Qual será o Booleano resultante dos seguintes códigos?

# In[11]:


# Responda antes de executar a célula
2 > 3
False


# In[12]:


# Responda antes de executar a célula
3 <= 2
False


# In[13]:


# Responda antes de executar a célula
3 == 2.0
False


# In[14]:


# Responda antes de executar a célula
3.0 == 3
True


# In[15]:


# Responda antes de executar a célula
4**0.5 != 2
False


# Pergunta final: qual é a saída booleana do bloco de código abaixo?
# False

# In[16]:


# Duas listas aninhadas
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# Verdadeiro ou falso?
l_one[2][0] >= l_two[2]['k1']
False

