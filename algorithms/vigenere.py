from algorithms.cipher import Cipher

class VigenereCipher(Cipher):
    def __init__(self,key):
        super().__init__()
        self.key = key

    def encrypt(self, plaintext, key):
        plaintext = self._preprocess_text(plaintext)
        key = self._preprocess_text(key)
        encrypted = []

        for i, char in enumerate(plaintext):
            if char in self.ukrainian_alphabet or char in self.english_alphabet:
                alphabet = self._get_alphabet(char)

                key_char = key[i % len(key)]
                shift = self._get_index(key_char, self.ukrainian_alphabet) if key_char in self.ukrainian_alphabet else self._get_index(key_char, self.english_alphabet)

                char_index = self._get_index(char, alphabet)

                encrypted_char = self._convert_to_char((char_index + shift) % len(alphabet), alphabet)
                encrypted.append(encrypted_char)
            else:
                encrypted.append(char)  

        return ''.join(encrypted)
