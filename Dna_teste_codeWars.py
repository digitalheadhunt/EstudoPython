def DNA_strand(dna):
    # code here
    final_dna = ''
    for cel in dna:
        if cel == 'A':
            final_dna += 'T'
        elif cel == 'T':
            final_dna +='A'
        elif cel == 'G':
            final_dna +='C'
        elif cel == 'C':
            final_dna += 'G'
        else:
            break
    print(final_dna) 
    return final_dna

DNA_strand('AATTGC')
            
    