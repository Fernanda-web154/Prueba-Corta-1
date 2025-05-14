import tkinter as tk
from cr import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="purple",
        padx=0,
        pady=0,
        width=1000,
        height=600
    )

    tk.Label(login_panel, text="Escriba el nombre que deseee").pack()
    entrada_dnombre = tk.Entry(login_panel, width=40)
    entrada_dnombre.pack(pady=10)

    def consultar():
        nombre = entrada_dnombre.get()
        consulta = f"SELECT edad, apellido FROM Alumnos WHERE nombre = '{nombre}'"
        resultado = conectar(consulta)

        if resultado:
            print("Datos encontrados:")
            for fila in resultado:
                print(f"Edad encontrada: {fila[0]}")
                print(f"Apellido encontrado: {fila[1]}")
        else:
            print("No se pudo encontrar lo solicitado en nuestra base de datos")


    boton_buscar = tk.Button(login_panel, text="Consultar", command=consultar)
    boton_buscar.pack(pady=15)

    login_panel.pack()
    print("Se cargó correctamente")



     
