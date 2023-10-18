import calendar
import tkinter as tk
import datetime

# Obtenemos los valores del año y mes a mostrar
año = datetime.date.today().year
mes = datetime.date.today().month
year = año
month = mes

def writeCalendar(year, month):
    # Limpia cualquier widget existente en el frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Asignamos el año y mes al calendario
    str1 = calendar.month(year, month)

    label1.configure(text=str1)

    # Crear un widget Label separado para cada número del calendario
    for i, day in enumerate(str1.split(), start=1):
        label = tk.Label(frame, text=day, font=('courier', 30, 'bold'), padx=5, pady=5, bg='white')
        label.grid(row=2 + (i - 1) // 7, column=(i - 1) % 7)
        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)

def mesAnterior():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1

    writeCalendar(year, month)

def mesSiguiente():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1

    writeCalendar(year, month)

def on_enter(event):
    event.widget.config(bg="lightblue")

def on_leave(event):
    event.widget.config(bg="white")

root = tk.Tk()
root.title("Calendario")

# Lo posicionamos en un label
label1 = tk.Label(root, text="", font=('courier', 30, 'bold'), bg='white', justify=tk.LEFT)
label1.grid(row=1, column=1)

# ponemos los botones dentro de un Frame
frame = tk.Frame(root, bd=5)
anterior = tk.Button(frame, text="Anterior", command=mesAnterior)
anterior.grid(row=1, column=1, sticky=tk.W)
siguiente = tk.Button(frame, text="Siguiente", command=mesSiguiente)
siguiente.grid(row=1, column=2)
frame.grid(row=2, column=1)

writeCalendar(year, month)

# ejecutamos el evento loop
root.mainloop()
