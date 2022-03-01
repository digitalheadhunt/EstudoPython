def camel_case(str):
    splited = str.replace(' ','')
    new_word =''
    if len(str)>1:
        for x in splited:
            x.lower()
            print(x)
            new_word += x.replace(x[0], x[0].upper())
            print(x)
    return new_word

#print(camel_case("hello world"))
print(camel_case("test cases"))
# print(camel_case("say hello "))