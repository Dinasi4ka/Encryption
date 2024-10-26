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

        self.header_font = Font(family="Arial", size=16, weight="bold")
        self.label_font = Font(family="Arial", size=12)

        self.frame = Frame(self.root, bg="#2c2f33", bd=5, relief=GROOVE)
        self.frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

        self.create_label("Choose Cipher Algorithm", self.header_font, pady=20)

        self.cipher_choice = StringVar(value="1")
        cipher_options = [
            ("Caesar Cipher", "1"),
            ("Vigenere Cipher", "2"),
            ("Gamma Cipher", "3"),
            ("RSA", "4")
        ]
        self.create_radio_buttons(cipher_options)

        self.text_entry = self.create_labeled_entry("Enter text to encrypt", "Example: hello")

        self.key_entry = self.create_labeled_entry("Enter Key or Shift", "Example: 2,3")

        self.create_button("Encrypt", self.encrypt)

        self.result_label = self.create_label("", pady=10)

        self.cipher_choice.trace("w", self.update_placeholders)

        self.update_placeholders()

    def create_label(self, text, font=None, pady=0):
        label = Label(self.frame, text=text, font=font or self.label_font, bg="#2c2f33", fg="#ffffff")
        label.pack(pady=pady, padx=10, fill=X)
        return label

    def create_radio_buttons(self, options):
        frame_cipher = Frame(self.frame, bg="#2c2f33")
        frame_cipher.pack(pady=10, fill=X)
        for text, value in options:
            Radiobutton(frame_cipher, text=text, variable=self.cipher_choice, value=value, font=self.label_font,
                        bg="#2c2f33", fg="#ffffff", selectcolor="#7289da").pack(anchor=W, padx=20)

    def create_labeled_entry(self, label_text, placeholder_text):
        label = Label(self.frame, text=label_text, font=self.label_font, bg="#2c2f33", fg="#ffffff")
        label.pack(pady=5, padx=10, fill=X)

        entry = Entry(self.frame, width=40, bd=3, bg="#23272a", fg="#aaaaaa", insertbackground="#ffffff", relief=FLAT)
        entry.pack(pady=5, padx=10, fill=X)
        entry.insert(0, placeholder_text)  

        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(entry, placeholder_text))
        entry.bind("<FocusOut>", lambda e: self.set_placeholder(entry, placeholder_text))

        return entry

    def create_button(self, text, command):
        button = Button(self.frame, text=text, command=command, font=self.label_font, bg="#7289da", fg="#ffffff",
                        activebackground="#5b6eae", activeforeground="#ffffff", relief=FLAT)
        button.pack(pady=20, padx=10, ipadx=10, ipady=5, fill=X)

    def update_placeholders(self, *args):
        cipher = self.cipher_choice.get()
        if cipher == '1':  
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: 2,3")
        elif cipher == '2': 
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: key")
        elif cipher == '3': 
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: key")
        elif cipher == '4':  
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, "Example: hello")
            self.key_entry.delete(0, END)
            self.key_entry.insert(0, "Example: 3, 13, 5")

    def set_placeholder(self, entry, placeholder_text):
        if not entry.get() or entry.get() == placeholder_text:  
            entry.delete(0, END)  
            entry.insert(0, placeholder_text)  
            entry.config(fg="#aaaaaa") 

    def clear_placeholder(self, entry, placeholder_text):
        if entry.get() == placeholder_text:  
            entry.delete(0, END) 
            entry.config(fg="#ffffff") 

    def encrypt(self):
        text = self.text_entry.get()
        choice = self.cipher_choice.get()

        if text == "Example: hello" or text == "": 
            self.display_error("Error: Please enter text to encrypt.")
            return

        if choice == '1': 
            shifts = self.key_entry.get().strip()
            try:
                shift_list = [int(shift.strip()) for shift in shifts.split(',')] 
            except ValueError as e:
                self.display_error("Error: Enter valid shifts as comma-separated numbers.")
                return
            cipher = CaesarCipher(shift_list)  
            encrypted = cipher.encrypt(text)

        elif choice == '2':  
            try:
                key = validate_vigenere_key(self.key_entry.get().strip())
                cipher = VigenereCipher(key)
                encrypted = cipher.encrypt(text, key)
            except ValueError as e:
                self.display_error(str(e))
                return

        elif choice == '3':
            try:
                key = validate_gamma_key(self.key_entry.get().strip())
                cipher = GammaCipher(key)
                encrypted = cipher.encrypt(text)
            except ValueError as e:
                self.display_error(str(e))
                return

        elif choice == '4': 
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

        self.result_label.config(text=f"Encrypted text: {encrypted}") 

    def display_error(self, message):
        messagebox.showerror("Error", message)


if __name__ == "__main__":
    root = Tk()
    app = CipherMenu(root)
    root.mainloop()