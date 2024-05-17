# Fahrenheit - Celsius Converter

import tkinter as tk
def my_conv():
    if var.get()==1:
        F = float(ent.get())
        C = 5/9*(F-32)
        lbl4["text"]=str(round(C,2))+" °C"
    else:
        C = float(ent.get())
        F = 9/5*C+32
        lbl4["text"]=str(round(F,2))+" °F"
        

def far2cel():
    lbl3["text"]="°F"
    
def cel2far():
    lbl3["text"]="°C"    

w = tk.Tk()
var = tk.IntVar()
var.set(2)
lbl1 = tk.Label(text="Input as")
lbl1.grid(row=0,column=0)
r1 = tk.Radiobutton(text="Fahrenheit (°F)", 
                    variable=var,
                    value = 1,
                    command=far2cel)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(text="Celsius (°C)", 
                    variable=var,
                    value = 2,
                    command=cel2far)
r2.grid(row=0, column=2)
lbl2 = tk.Label(text="Input")
lbl2.grid(row=1,column=0)
ent = tk.Entry()
ent.grid(row=1,column=1)
lbl3 = tk.Label(text="°C")
lbl3.grid(row=1,column=2)
btn = tk.Button(text="Convert", command=my_conv)
btn.grid(row=2,column=0)
lbl4 = tk.Label()
lbl4.grid(row=2,column=1)
w.mainloop()
