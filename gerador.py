import random

def gera_numeros():
    # Gera três números aleatórios
    numero1 = random.randint(1, 50)
    numero2 = random.randint(1, 50)
    numero3 = random.randint(1, 50)
    
    # Põe os números em uma lista
    numeros = [numero1, numero2, numero3]
    
    # Escolhe dois números aleatórios da lista
    index1 = random.randint(0, 2)
    index2 = random.randint(0, 2)
    while index2 == index1:
        index2 = random.randint(0, 2)
    
    # Soma os dois números escolhidos
    numero_total = numeros[index1] + numeros[index2]
    
    # Encontra o índice do número que não faz parte da soma
    for i in range(3):
        if i != index1 and i != index2:
            index_fora = i
            break
    
    return numeros + [numero_total, index_fora]
