"""
Create a function that takes one element;
this element will be an morse code;
Translate this code to human readable;
"""


def decode_morse(morse):
    MORSE_CODE = {
        '.-': 'A',
        '-…': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '….': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '…': 'S',
        '-': 'T',
        '..-': 'U',
        '…-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-----': '0',
        '.----': '1',
        '..---': '2',
        '…--': '3',
        '….-': '4',
        '…..': '5',
        '-….': '6',
        '--…': '7',
        '---..': '8',
        '----.': '9',
    }
    return 0


print(decode_morse('.... . -.--   .--- ..- -.. .'))