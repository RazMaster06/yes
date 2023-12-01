char_to_numb = {
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E',
    'E': 'F',
    'F': 'G',
    'H': 'I',
    'I': 'J',
    'J': 'K',
    'K': 'L',
    'L': 'M',
    'M': 'N',
    'N': 'O',
    'O': 'P',
    'P': 'Q',
    'Q': 'R',
    'R': 'S',
    'S': 'T',
    'T': 'U',
    'U': 'V',
    'V': 'W',
    'W': 'X',
    'X': 'Y',
    'Y': 'Z',
    'Z': 'Å',
    'Å': 'Ä',
    'Ä': 'Ö',
}

while True:
    text = input("Mata in text: ").upper()
    converted_text = ""

    for i in range(len(text)):
        key = text[i]
        svar = char_to_numb.get(key)
        converted_text += svar + ""

    print(converted_text)
