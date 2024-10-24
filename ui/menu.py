# cipher_menu.py

from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from algorithms.caesar import CaesarCipher
from algorithms.vigenere import VigenereCipher
from algorithms.gamma import GammaCipher
from algorithms.rsa import RSACipher
from validation import validate_gamma_key, validate_rsa_keys, validate_vigenere_key

class CipherMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption Menu")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c2f33")

        # Налаштування шрифтів
        self.header_font = Font(family="Arial", size=16, weight="bold")
        self.label_font = Font(family="Arial", size=12)

        # Основний фрейм з рамкою
        self.frame = Frame(self.root, bg="#2c2f33", bd=5, relief=GROOVE)
        self.frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        # Заголовок
        self.create_label("Choose Cipher Algorithm", self.header_font, pady=20)

        # Створення радіокнопок для вибору шифру
        self.cipher_choice = StringVar(value="1")
        cipher_options = [
            ("Caesar Cipher", "1"),
            ("Vigenere Cipher", "2"),
            ("Gamma Cipher", "3"),
            ("RSA", "4")
        ]
        self.create_radio_buttons(cipher_options)

        # Поле для введення тексту
        self.text_entry = self.create_labeled_entry("Enter text to encrypt", "Example: hello")

        # Поле для введення ключа
        self.key_entry = self.create_labeled_entry("Enter Key or Shift", "Example: 2,3")

        # Кнопка для шифрування
        self.create_button("Encrypt", self.encrypt)

        # Виведення результату
        self.result_label = self.create_label("", pady=10)

        # Оновлення підказок при зміні вибору шифру
        self.cipher_choice.trace("w", self.update_placeholders)

        # Встановлення початкових підказок
        self.update_placeholders()

    # Допоміжна функція для створення міток
    def create_label(self, text, font=None, pady=0):
        label = Label(self.frame, text=text, font=font or self.label_font, bg="#2c2f33", fg="#ffffff")
        label.pack(pady=pady, padx=10, fill=X)
        return label

    # Допоміжна функція для створення радіокнопок
    def create_radio_buttons(self, options):
        frame_cipher = Frame(self.frame, bg="#2c2f33")
        frame_cipher.pack(pady=10, fill=X)
        for text, value in options:
            Radiobutton(frame_cipher, text=text, variable=self.cipher_choice, value=value, font=self.label_font,
                        bg="#2c2f33", fg="#ffffff", selectcolor="#7289da").pack(anchor=W, padx=20)

    # Допоміжна функція для створення міток і полів введення
    def create_labeled_entry(self, label_text, placeholder_text):
        # Створення мітки
        label = Label(self.frame, text=label_text, font=self.label_font, bg="#2c2f33", fg="#ffffff")
        label.pack(pady=5, padx=10, fill=X)

        # Створення поля вводу
        entry = Entry(self.frame, width=40, bd=3, bg="#23272a", fg="#aaaaaa", insertbackground="#ffffff", relief=FLAT)
        entry.pack(pady=5, padx=10, fill=X)
        entry.insert(0, placeholder_text)  # Вставлення підказки в поле вводу

        # Видалення підказки при фокусуванні
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, placeholder_text))
        entry.bind("<FocusOut>", lambda e: self.set_placeholder(entry, placeholder_text))

        return entry

    # Допоміжна функція для створення кнопок
    def create_button(self, text, command):
        button = Button(self.frame, text=text, command=command, font=self.label_font, bg="#7289da", fg="#ffffff",
                        activebackground="#5b6eae", activeforeground="#ffffff", relief=FLAT)
        button.pack(pady=20, padx=10, ipadx=10, ipady=5, fill=X)

    # Функція для оновлення підказок
    def update_placeholders(self, *args):
        cipher = self.cipher_choice.get()
        if cipher == '1':  # Caesar Cipher
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: 2,3")
        elif cipher == '2':  # Vigenère Cipher
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: key")
        elif cipher == '3':  # Gamma Cipher
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: key")
        elif cipher == '4':  # RSA Cipher
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: message")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: 3, 13, 5")

    # Оновлення підказки при втраті фокусу
    def set_placeholder(self, entry, placeholder_text):
        if not entry.get() or entry.get() == placeholder_text:  # Якщо поле пусте або текст відповідає підказці
            entry.delete(0, END)  # Очищаємо поле
            entry.insert(0, placeholder_text)  # Вставляємо підказку
            entry.config(fg="#aaaaaa")  # Змінюємо колір тексту на сірий

    # Очищення підказки при фокусуванні
    def clear_placeholder(self, entry, placeholder_text):
        if entry.get() == placeholder_text:  # Якщо текст відповідає підказці
            entry.delete(0, END)  # Очищаємо поле
            entry.config(fg="#ffffff")  # Змінюємо колір тексту на білий

    # Функція для шифрування
    def encrypt(self):
        text = self.text_entry.get()
        choice = self.cipher_choice.get()

        if text == "Example: hello" or text == "":  # Якщо введений текст відповідає підказці
            self.display_error("Error: Please enter text to encrypt.")
            return

        if choice == '1':  # Caesar Cipher
            shifts = self.key_entry.get().strip()
            try:
                shift_list = [int(shift.strip()) for shift in shifts.split(',')]  # Виконуємо шифрування
            except ValueError as e:
                self.display_error("Error: Enter valid shifts as comma-separated numbers.")
                return
            cipher = CaesarCipher(shift_list)  # Створюємо об'єкт шифру Цезаря з кількома зсувами
            encrypted = cipher.encrypt(text)

        elif choice == '2':  # Vigenère Cipher
            try:
                key = validate_vigenere_key(self.key_entry.get().strip())
                cipher = VigenereCipher(key)
                encrypted = cipher.encrypt(text, key)
            except ValueError as e:
                self.display_error(str(e))
                return

        elif choice == '3':  # Gamma Cipher
            try:
                key = validate_gamma_key(self.key_entry.get().strip())
                cipher = GammaCipher(key)
                encrypted = cipher.encrypt(text)
            except ValueError as e:
                self.display_error(str(e))
                return

        elif choice == '4':  # RSA Cipher
            try:
                p, q, exponent = self.key_entry.get().split(',')
                p, q, exponent = validate_rsa_keys(p.strip(), q.strip(), exponent.strip())
                cipher = RSACipher(p, q, exponent)
                encrypted = cipher.encrypt(text)
            except ValueError as e:
                self.display_error(str(e))
                return
            except ZeroDivisionError:
                self.display_error("Error: Division by zero occurred during encryption.")
                return
            except Exception as e:
                self.display_error(f"Error: {str(e)}")
                return

        self.result_label.config(text=f"Encrypted text: {encrypted}")  # Відображення результату

    # Функція для відображення помилок
    def display_error(self, message):
        messagebox.showerror("Error", message)


# Головна функція
if __name__ == "__main__":
    root = Tk()
    app = CipherMenu(root)
    root.mainloop()
