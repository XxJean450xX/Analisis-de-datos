import tkinter as tk
from tkinter import filedialog
import pandas as pd
import statistics

# Crear una ventana
root = tk.Tk()
#-------------Variables------------------------

#-------------Seleccionar Archivo----------------

# Definir una función para abrir el diálogo de archivos
def open_file():
    # Abrir un diálogo para seleccionar un archivo CSV
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=(("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
    )
    if file_path:
        # Leer el archivo CSV y mostrar algunas filas
        df = pd.read_csv(file_path)
        print("Archivo CSV cargado:")
        print(df.head(20))  # Mostrar las primeras 20 filas

# Botón para cargar el archivo
load_button = tk.Button(root, text="¡Sube tu archivo csv!", command=open_file)
load_button.pack(pady=50)

#-------------Medidas de Tencia Centra--------------

def promedio(i):
    return sum(i)/len(i)
    
def moda(i):
    return statistics.mode(i)

def media(i):
    proof = len(i)%2
    if proof == 0:
        ind_left = (len(i)//2)-1
        ind_right = len(i)//2
        dat_central = i[ind_left:ind_right + 1]
        dat_central = sum(dat_central)/2
        return round(dat_central)
    else:
        ind = len(i)//2
        dat_central = i[ind]
        return dat_central

#-------------Cuartiles-Percentiles-Deciles---------------

def cuartil(i):
    totaldedatos = len(i)
    proof = len(i)%2
    cuartiles = []
    if proof == 0:
        for x in range(1,4):
            percent = (x * totaldedatos)/4
            percent = round(percent)
            percent = int(i[percent - 1])
            cuartiles.append(percent)
        return cuartiles
    else:
        for x in range(1,4):
            percent = (x * (1 + totaldedatos))/4
            percent = round(percent)
            percent = int(i[percent- 1])
            cuartiles.append(percent)
        return cuartiles
        
def deciles(i):
    totaldedatos = len(i)
    proof = len(i)%2
    cuartiles = []
    if proof == 0:
        for x in range(1,11):
            percent = (x * totaldedatos)/4
            percent = round(percent)
            percent = int(i[percent - 1])
            cuartiles.append(percent)
        return cuartiles
    else:
        for x in range(1,11):
            percent = (x * (1 + totaldedatos))/4
            percent = round(percent)
            percent = int(i[percent- 1])
            cuartiles.append(percent)
        return cuartiles
    
def percentiles(i):
    totaldedatos = len(i)
    proof = len(i)%2
    cuartiles = []
    if proof == 0:
        for x in range(1,101):
            percent = (x * totaldedatos)/100
            percent = round(percent)
            percent = int(i[percent - 1])
            cuartiles.append(percent)
        return cuartiles
    else:
        for x in range(1,101):
            percent = (x * (1 + totaldedatos))/100
            percent = round(percent)
            percent = int(i[percent- 1])
            cuartiles.append(percent)
        return cuartiles
    
root.mainloop()