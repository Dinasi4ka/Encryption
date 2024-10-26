import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'algorithms')))


from ui.menu import CipherMenu
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x600") 
    app = CipherMenu(root)
    root.mainloop()
