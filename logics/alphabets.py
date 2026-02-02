from logics.base import EncryptionLogic

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.'
}
MORSE_DECODE = {v: k for k, v in MORSE_CODE.items()}


class MorseCodeLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "morse"

    @property
    def description(self) -> str:
        return "Morse code encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        encoded = ' '.join(MORSE_CODE.get(c, c) for c in text)
        return encoded.encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        morse = data.decode('utf-8', errors='replace')
        decoded = ''.join(MORSE_DECODE.get(c, c) for c in morse.split(' '))
        return decoded.encode('utf-8')


NATO_ALPHABET = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu', '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
    '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
    ' ': '/'
}
NATO_DECODE = {v.upper(): k for k, v in NATO_ALPHABET.items()}


class SpellingAlphabetLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "nato"

    @property
    def description(self) -> str:
        return "NATO phonetic alphabet"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        encoded = ' '.join(NATO_ALPHABET.get(c, c) for c in text)
        return encoded.encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        # Split by spaces but handle multiple spaces
        parts = data.decode('utf-8', errors='replace').split()
        result = []
        for p in parts:
            val = NATO_DECODE.get(p.upper())
            if val:
                result.append(val)
            else:
                # If not in dictionary, keep original if single char or skip
                if len(p) == 1:
                    result.append(p)
                elif p == '/':
                    result.append(' ')
        return ''.join(result).encode('utf-8')
