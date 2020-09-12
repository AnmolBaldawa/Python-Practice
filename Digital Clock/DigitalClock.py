import time
import tkinter

tkObject = tkinter.Tk()
tkObject.title("Digital Clock")
tkObject.geometry("500x200+0+0")
tkObject.resizable(True, True)
label = tkinter.Label(master=tkObject, background='yellow', font=('Chiller', 30, 'bold'))
label.grid(row=0, column=1)


def func():
    label.config(text="Time is " + time.strftime("%I:%M:%S %p"))
    label.after(ms=500, func=func)


func()
tkObject.mainloop()
