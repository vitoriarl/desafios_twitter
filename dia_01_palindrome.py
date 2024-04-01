# DIA 1 - PALÍNDROMO

print("Hellouu! ")
resposta = input("Digite uma palavra e eu te digo se ela é um palindromo ou não: ")

def coloca_ao_contrario(palavra): 
    tamanho = len(palavra) - 1
    contrario = ''
    while tamanho >= 0:
        contrario = contrario + palavra[tamanho]
        tamanho = tamanho - 1
    return contrario

palavra_ao_contrario = coloca_ao_contrario(resposta)

if palavra_ao_contrario == resposta:
    print(f"A palavra que você digitou é {resposta} e ao contrário fica {palavra_ao_contrario} \n")
    print("Por isso, a palavra é um palíndromo!")
else:
    print(f"A palavra que você digitou é {resposta} e ao contrário fica {palavra_ao_contrario} \n")
    print("Por isso, a palavra NÃO é um palíndromo!")
