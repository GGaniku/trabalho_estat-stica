from main import *
import matplotlib.pyplot as plt
import numpy as np

data = []

# Escolher entre inserir um novo banco de dados ou utilizar o que coletei para o trabalho

'''a = int(input('Você quer fazer os cálculos a partir de um \033[32mnovo banco de dados\033[m [1] ou a partir do \033[32mBD já inserido no sistema\033[m [2]? '))
if a == 1:
    print('NOVO BANCO DE DADOS:')
    while True:
        insert_data = int(input('Insira, aqui, seus dados brutos [0 para sair]: '))
        if insert_data != 0:
            data.append(insert_data)
        elif insert_data == 0:
            print('Inserção de dados realizada com sucesso.')
            break'''
a = 2
if a == 2:
    print('USAR O BANCO DE DADOS NO SISTEMA:')
    data = [18, 19, 24, 19, 18, 18, 18, 20, 22, 18, 18, 18, 18, 20, 21, 18, 18, 18, 19, 17, 18, 17, 19, 19, 19, 17, 17, 20, 19, 34, 18, 19, 19, 19, 18]

print(f'''Dados brutos: {data}
Quantidade de dados: {len(data)}''')

# Ordenar as observações da variável escolhida:

data = sorted(data)
print(f'Os dados ordenados em ordem crescente é: {data}')

# Determinar a média entre as observações:

media_dados = media(data)
print(f'a média é: {media_dados}')

## Fazer a Distribuição de frequência!:

#   Tirar as observações repetidas da variável:

#frequencias = no_rep(data)
#print(f'''Frequências: {frequencias}
#Número de frequência: ''')
freq = frequency(data)
print(freq)
#   

# Calcular a 

'''y = enumerate(len(data))
plt.scatter(data,y)
plt.show()'''

'''print(list(numpy.digitilize()))'''
'''print(list.index(data))'''