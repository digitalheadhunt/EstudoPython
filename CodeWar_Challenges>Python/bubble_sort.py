def bubble(vetor):
    iteracoes = len(vetor)
    auxValue = ''
    print(type(vetor))
    for x in range(iteracoes):
        for j in range(0,iteracoes - x - 1):
            if vetor[j] > vetor[j+1]:
                print('-------')
                print(vetor[j])
                print(vetor[j+1])
                print('--------')
                
                auxValue = vetor[j+1]
                vetor[j+1] = vetor[j]
                vetor[j] = auxValue;
                auxValue = ''
    return vetor
   
   
arr = [100,2,3,7,15,26,1,0,4,6,8,99,90,11] 
print(bubble(arr))     