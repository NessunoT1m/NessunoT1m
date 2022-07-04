from tkinter import*
from tkinter.ttk import*
from time import strftime

main = Tk()

main.title('The digital time  Python')

def clock():
    tick = strftime('%H:%H:%S %p')
    clock_label.config(text = tick)
    clock_label.after(100, clock)

clock_label = Label(main, font=('sans', 80), background='red', foreground='white')

clock_label.pack(anchor='center')
clock()
mainloop()
