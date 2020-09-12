import time
import tkinter

tkObject = tkinter.Tk()
tkObject.title("Digital Clock")
tkObject.geometry("500x200+0+0")  # Size and position of the pop-up window
tkObject.resizable(True, True)
label = tkinter.Label(master=tkObject, background='yellow', font=('Chiller', 30, 'bold'))
label.grid(row=0, column=1)


def func():
    label.config(text="Time is " + time.strftime("%I:%M:%S %p"))
    label.after(ms=500, func=func)  # Change the ms(milliseconds) to vary the update time of clock


func()
tkObject.mainloop()
