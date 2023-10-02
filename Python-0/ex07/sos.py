import sys


def main():
    text = sys.argv
    assert len(text) == 2, "arguments invalid"
    assert text[1].isalnum(), "invalid string"
    morse = {" ": "/",
             "A": ".- ", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
             'J': '.---', 'K': '.-..', 'L': '.-..', 'M': '--',
             'N': '-.', 'O': '---', 'P': '.---.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
             'V': '..-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
             'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...',
             '8': '---..', '9': '----.', '0': '-----'}   
    morse_list = [morse[char.upper()] for char in text[1] if char.upper() in morse]
    morse_string = " ".join(morse_list)
    print(morse_string)