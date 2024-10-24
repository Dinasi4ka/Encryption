from tkinter import Radiobutton, StringVar
from algorithms.caesar import CaesarCipher
from algorithms.vigenere import VigenereCipher
from algorithms.gamma import GammaCipher
from algorithms.rsa import RSACipher

class CipherSelection:
    def __init__(self, root):
        self.root = root
        self.cipher_choice = StringVar(value="1")
        self.ciphers = {
            "1": CaesarCipher,
            "2": VigenereCipher,
            "3": GammaCipher,
            "4": RSACipher
        }
        self.create_cipher_radio_buttons()

    def create_cipher_radio_buttons(self):
        options = {
            "1": "Цезар",
            "2": "Віженер",
            "3": "Гамма",
            "4": "RSA"
        }
        for index, (value, name) in enumerate(options.items(), start=1):
            button = Radiobutton(self.root, text=name, variable=self.cipher_choice, value=value)
            button.grid(row=index, column=0, sticky='w')

    def get_selected_cipher(self):
        return self.ciphers.get(self.cipher_choice.get())
