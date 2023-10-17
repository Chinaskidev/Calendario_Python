import calendar
import tkinter as tk
import datetime

# Obtenemos los valores del año y mes a mostrar
año = datetime.date.today().year
mes = datetime.date.today().month
year= año
month= mes
 
def writeCalendar(year,month):
	# Asignamos el año y mes al calendario
	str1 = calendar.month(year, month)
 
	label1.configure(text=str1)
 
def mesAnterior():
	global month,year
	month-=1
	if month==0:
		month=12
		year-=1
 
	writeCalendar(year,month)
 
def mesSiguiente():
	global month,year
	month+=1
	if month==13:
		month=1
		year+=1
 
	writeCalendar(year,month)
 
def on_enter(event):
    event.widget.config(bg="lightblue")

def on_leave(event):
    event.widget.config(bg="white")

 
root = tk.Tk()
root.title("Calendario")
 
# Lo posicionamos en un label
label1 = tk.Label(root, text="", font=('courier', 30, 'bold'), bg='white', justify=tk.LEFT)
label1.grid(row=1,column=1)
 
# ponemos los botones dentro un Frame
frame=tk.Frame(root,bd=5)
anterior = tk.Button(frame,text="Anterior", command=mesAnterior)
anterior.grid(row=1, column=1, sticky=tk.W)
siguiente = tk.Button(frame,text="Siguiente", command=mesSiguiente)
siguiente.grid(row=1, column=2)
frame.grid(row=2,column=1)
 
writeCalendar(year,month)
label1.bind("<Enter>", on_enter)
label1.bind("<Leave>", on_leave)

 
# ejecutamos el evento loop
root.mainloop()