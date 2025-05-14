import tkinter as tk 
from arriba import cargar_arriba
from login import cargar_login
from add import cargar_add
#VENTANA DE LA APLICACIÓN
ventana = tk.Tk()
ventana.title("mi tienda")
ventana.geometry("800x600")

#MÓDULOS DE LA VENTANA
cargar_login(ventana)

ventana.mainloop()