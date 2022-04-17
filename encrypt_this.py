"""
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.

"""

def encrypt_this(str):
    splited = str.split(' ')
    for ele in splited:
        ele = list(ele)
        second = ele[1]
        last = ele[-1]
        ele[1] = last
        ele[-1] = second 
        ele = ele.replace(ele[0], ord(ele[0]))
        
    print(splited)
    return ' '.join(splited)

print(encrypt_this('hello world'))