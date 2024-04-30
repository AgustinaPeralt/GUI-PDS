import tkinter as tk
from tkinter import *
from tkinter import ttk, Frame, Button, Label 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt 
import subprocess

#funciones de procesamiento
#def iniciarmuestreo():
 #   global proceso
 #   proceso = subprocess.Popen(["notepad.exe"])

#def finalizarmuestreo():
#    if 'proceso' in globals() and proceso.poll() is None:
#       proceso.terminate()

#Instancia de la clase Tk
#ventana1=tk.Tk()
#ventana1.title("Visualizador de señales")

#Variables que almacenarán los datos
#start = StringVar()
#finish = StringVar()

#generación de widgets


#boton
#boton_iniciar = tk.Button(ventana1, text="Iniciar muestreo", command=iniciarmuestreo)
#boton_iniciar.grid(row=8, column=1)

#boton_parar = tk.Button(ventana1, text="Finalizar muestreo", command=finalizarmuestreo)
#boton_parar.grid(row=8, column=3)

#Gráfica matplotlib scale
fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor='#00faafb7')
plt.title("Grafica que permite visualizar la señal muestreada",color='red',size=16, family="Arial")

plt.xlim(-4, 14)
plt.ylim(-8, 8)
ax.set_facecolor('black')

ax.axhline(linewidth=2, color='r')
ax.axvline(linewidth=2, color='r')

ax.set_xlabel("Frecuencia", color='black')
ax.set_ylabel("Amplitud", color='black')
ax.tick_params(direction='out', length=6, width=2, 
	colors='black',
    grid_color='r', grid_alpha=0.5)

def graficar_datos():
	nivel = scale.get()
	x = np.arange(-np.pi, 4*np.pi, 0.01) 	
	line, = ax.plot(x, nivel*np.sin(x), 
		color ='b', linestyle='solid')
	canvas.draw()
	label.config(text= nivel)
	line.set_ydata(np.sin(x)+10)
	ventana.after(100, graficar_datos)

ventana = Tk()
ventana.geometry('642x498')
ventana.wm_title('Grafica Matplotlib con Scale')
ventana.minsize(width=642,height=495)

frame = Frame(ventana,  bg='gray22',bd=3)
frame.grid(column=0,row=0)

canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.get_tk_widget().grid(column=0, row=0, columnspan=3, padx=5, pady =5)

Button(frame, text='Iniciar muestreo', width = 15, bg='magenta',fg='white', command= graficar_datos).grid(column=0, row=1, pady =5)
label = Label(frame, width = 15)
label.grid(column=1, row=1, pady =5)

#Button(frame, text='Finalizar muestreo', width = 15, bg='magenta',fg='white', command= graficar_datos).grid(column=0, row=1, pady =5)
#label = Label(frame, width = 15)
#label.grid(column=3, row=1, pady =5)

scale = ttk.Scale(frame, to = 6, from_ =0, orient='horizontal', length=300)
scale.grid(column=2, row=1)

style = ttk.Style()
style.configure("Horizontal.TScale", background= 'gray22')  
ventana.mainloop()

#ejecución de ventana
#ventana1.mainloop()