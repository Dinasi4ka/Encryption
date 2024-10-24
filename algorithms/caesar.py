from algorithms.cipher import Cipher

class CaesarCipher(Cipher):
    def __init__(self, shifts):
        super().__init__()
        self.shifts = [int(shift) for shift in shifts]  

    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)
        alphabet = self._get_alphabet(plaintext)
        result = []
        shift_len = len(self.shifts)

        for i, char in enumerate(plaintext):
            if char in alphabet:
                shift = self.shifts[i % shift_len]  
                index = (self._get_index(char, alphabet) + shift) % len(alphabet)
                encrypted_char = self._convert_to_char(index, alphabet)  
                result.append(encrypted_char)
            else:
                result.append(char)  

        return ''.join(result)
