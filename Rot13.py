def rot13(word):
    first_list =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","A","B","C","D","E","F","G","H","I","J","K","L","M"]
    second_list = ["n","o","p","q","r","s","t","u","v","w","x","y","z","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_string = ""
    index = 0
    for ele in word:
        if ele in first_list:
            index = first_list.index(ele)
            new_string += second_list[index]
        elif ele in second_list:
            index = second_list.index(ele)
            new_string +=first_list[index]
        elif ele not in first_list or ele not in second_list:
            new_string += ele;
    print(new_string)
    return new_string

rot13("thalis")
rot13("fernandes")
rot13("Teste")
rot13("testA12")
            
    