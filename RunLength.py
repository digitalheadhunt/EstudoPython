from collections import OrderedDict
def RunLength(strParam):
  #TRANSFORMA A str em um dicionario python de tuplas
  #com contendo os elementos como key e values   
  dict = OrderedDict.fromkeys(strParam,0)
  result = dict
  # agora iremos iterar sobre os elementos da string para percorrer e dizer quantos elementos tem iguais
  # como as keys do dicionario são iguais aos elementos da str iremos adicionar a key refente ao elemento o valor
  
  for ch in strParam:
    dict[ch] += 1
  output = '' 
  # aqui iremos iterar entre as tuplas e adicionar valor e chave a uma str e depois retornar essa str
  for key,value in dict.items():
    output = output + str(value) + key
  
  return output
