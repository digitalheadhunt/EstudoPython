"""
^               # start of input 
(?=.*?[A-Z])    # Lookahead to make sure there is at least one upper case letter
(?=.*?[a-z])    # Lookahead to make sure there is at least one lower case letter
(?=.*?[0-9])    # Lookahead to make sure there is at least one number
[A-Za-z0-9]{6,} # Make sure there are at least 6 characters of [A-Za-z0-9]
$               # end of input

"""

import re

def regex(str):
    return re.match("/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$/",str)

print(regex("Fa90Ti"))