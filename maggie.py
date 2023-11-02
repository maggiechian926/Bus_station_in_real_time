import tkinter as tk
from messageWindow import Display




class Window(tk.Tk):
    def __init__(self):
        super().__init__()








if __name__ == "__main__":
    window = Window()
    window.resizable(0,0) #無法改變視窗大小
    window.geometry("+600+600")
    window.mainloop()