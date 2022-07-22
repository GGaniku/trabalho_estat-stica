def media(data_list):
    n = len(data_list)
    sumlist = sum(data_list)
    return sumlist / n

def no_rep(myList):
    resultantList = []
    for element in myList:
        if element not in resultantList:
            resultantList.append(element)
    return resultantList

def frequency(myList):
    freq = []
    for element in myList:
        if element in freq:
            freq[element] += 1
        '''else:
            freq[element] = 1'''
    return freq

'''def frequency(my_list): 
    import numpy as np
    freq = {}
    # Função "unique" retorna um array com todos elementos existentes
    # uma única vez (sem repetição).
    for item in np.unique(np.array(my_list)):
        # Pesquisa na lista a frequencia de cada elemento
        # A função "where" retorna um array com os índices onde ocorre o item.
        # A ideia é só usar o tamanho desse array que sabemos a frequência.
         freq[item] = np.where(np.array(my_list)==item)[0].shape[0]

    for key, value in freq.items():
        print (f"{key} : {value}")

    return frequency(my_list)'''