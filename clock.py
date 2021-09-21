from tkinter import *
from tkinter.ttk import *
from time import strftime, strptime
from time import strptime
root = Tk()
root.title('My Digital Clock')
label = Label(root, font=('ALGERIAN', 100),
              background="#65000A", foreground="#C89F24")
label.pack(anchor='center')


def getTime():
    timevalue_24hour = strftime('%H : %M : %S ')

    t = strptime(timevalue_24hour, "%H : %M : %S ")

    timevalue_12hour = strftime("%I : %M : %S %p", t)

    label.config(text=timevalue_12hour)
    label.after(1000, getTime)


getTime()

mainloop()
