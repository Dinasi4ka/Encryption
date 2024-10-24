from abc import ABC, abstractmethod

class Cipher(ABC):
    def __init__(self):
        self.ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        self.english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def _get_alphabet(self, text):
        if any(char in self.ukrainian_alphabet for char in text):
            return self.ukrainian_alphabet
        return self.english_alphabet

    def _preprocess_text(self, text):
        return text.upper()  

    def _get_index(self, char, alphabet):
        return alphabet.index(char)

    def _convert_to_char(self, index, alphabet):
        return alphabet[index]
    
    def _convert_to_num(self, char):
        alphabet = self._get_alphabet(char)
        return self._get_index(char, alphabet) + 1

    @abstractmethod
    def encrypt(self, plaintext):
        pass


