#Conjuntos

- conjuntos em qualquer linguagem de programacao, estamos fazendo referencia a teoria dos conjuntos da matematica.
- no python os conjuntos sao chamados de sets.

 - da mesma forma que na matematica, os conjuntos(sets) nao possuem valores duplicados;
 - sets nao possuem valores ordenados;
 - elementos n sao acessados por indice, conjuntos nao sao indexados;
 
- conjuntos sao bons para utilizar quando, precisamos armazenar elementos mas nao nos importamos com a ordenacao deles, quando n precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos sao referenciados em python com {}

Diferenca entre conjuntos(sets) e mapas(Dict) em python:
    - Dicionario tem chave/valor;
    - conjunto tem apenas valor;



## Como definir um conjunto

### Forma 1

 s = set({1,2,3,4,5,6,7,2,5,4,3})

  ```
    OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente o mesmo sera ignorado sem gerar erro
    e nao fara parte do conjunto.
  ```


### Forma 2
    s = {1,2,3,4,5,6,3,2,4,5,6,7,8}


### Importante lembrar que alem de n ter elementos repetidos, os sets n tem ordem

    lista = [99,2,3,4,5,6,7,87,200]
    tupla = (99,2,3,4,5,6,7,87,200)
    dict = (lista, 'dict')


### Em sets podemos colocar todos os tipos de dados misturados

 s = {1, true, "teste", 1.3}


# Usos interesantes com sets


## Sets 
 
