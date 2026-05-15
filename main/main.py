import tkinter as tk
from interfaz.ventana_principal import AppColas

if __name__ == "__main__":
    root = tk.Tk()
    app = AppColas(root)
    root.mainloop()