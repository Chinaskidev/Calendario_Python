import calendar
import tkinter as tk
import datetime

año = datetime.date.today().year
mes = datetime.date.today().month
year = año
month = mes

def Calendario(year, month):
    str1 = calendar.month(year, month)
    label1.configure(text=str1)

def mesAnterior():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    Calendario(year, month)

def mesSiguiente():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    Calendario(year, month)

def mostrar_fecha():
    fecha = f"{month}/{year}"  # Formato de fecha (puedes ajustarlo según tus preferencias)
    entry_fecha.delete(0, tk.END)  # Borra el contenido actual del Entry
    entry_fecha.insert(0, fecha)  # Inserta la nueva fecha

root = tk.Tk()
root.title("Calendario")

label1 = tk.Label(root, text="", font=('courier', 14, 'bold'), bg='white', justify=tk.LEFT)
label1.grid(row=1, column=1)

frame = tk.Frame(root, bd=5)
anterior = tk.Button(frame, text="Anterior", command=mesAnterior)
anterior.grid(row=1, column=1, sticky=tk.W)
siguiente = tk.Button(frame, text="Siguiente", command=mesSiguiente)
siguiente.grid(row=1, column=2)
frame.grid(row=2, column=1)

entry_fecha = tk.Entry(root, font=('courier', 14, 'bold'))
entry_fecha.grid(row=3, column=1)

mostrar_fecha()

root.mainloop()
