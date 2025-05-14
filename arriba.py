import tkinter as tk

def cargar_arriba(ventana):
    header_panel = tk.Frame(
        ventana,
        bg="black",
        padx=0,
        pady=0,
        width=1000,
        height=60
    )
    header_panel.pack()