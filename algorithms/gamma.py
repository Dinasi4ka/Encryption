from algorithms.cipher import Cipher

class GammaCipher(Cipher):
    def __init__(self, key):
        super().__init__()
        self.key = self._preprocess_text(key)  

    def encrypt(self, plaintext):
        plaintext = self._preprocess_text(plaintext)
        alphabet = self._get_alphabet(plaintext)
        result = []

        for i, char in enumerate(plaintext):
            if char in alphabet:
                key_char = self.key[i % len(self.key)]  
                encrypted_char = self._convert_to_char(
                    (self._get_index(char, alphabet) + self._get_index(key_char, alphabet)) % len(alphabet),
                    alphabet  
                )
                result.append(encrypted_char)
            else:
                result.append(char)  

        return ''.join(result)

