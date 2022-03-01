print('Nome do aluno:')
nome = input('digite o nome do aluno:')
nota = input('digite a nota do aluno:')

with open('./relacaonotas.txt','a') as text:
    text.write('\n Aluno:'+nome +' '+'Nota:'+ nota+'\n')